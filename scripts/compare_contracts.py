#!/usr/bin/env python3

from __future__ import annotations

import difflib
import json
import os
from dataclasses import asdict, dataclass, field, fields
from enum import Enum
from functools import cached_property, lru_cache
from itertools import starmap, zip_longest
from pathlib import Path
from pprint import pprint
from typing import Iterable, Callable, Iterable, Any

import requests
from solidity_parser import parser

Address = str

API_ENDPOINT = "https://api.polygonscan.com/api"
API_KEY = os.environ.get("POLYGONSCAN_API_KEY")
API_MODULE = "contract"

# Two similar looking but different OvixChainlinkOracleV2 contracts on polygon PoS
CONTRACT_ADDRESSES = [
    "0x421FF03Fe1085bce50ec5Bf06c5907119d87672F",
    "0x1c312b14c129eabc4796b0165a2c470b659e5f01",
]
addresses = CONTRACT_ADDRESSES


# utility functions
def map_starmap(func: Callable[..., Any], iterable_of_kwargs: Iterable[dict]) -> map:
    return map(lambda kv: func(**kv), iterable_of_kwargs)


def are_all_instances_of(*args: object, type: type) -> bool:
    return all(isinstance(arg, type) for arg in args)


def clean_code(s: str) -> str:  # else cannot use json.loads
    return s.replace("{{", "{").replace("}}", "}")


def data_diff(d1: Union[list, dict], d2: Union[list, dict]) -> dict:
    diff = {}
    # dictionary keys are sorted by order of insertion since python3.7
    if are_all_instances_of(d1, d2, type=list):  # integer keys
        d1, d2 = dict(enumerate(d1)), dict(enumerate(d2))
    for k in d1.keys() | d2.keys():
        v1, v2 = d1.get(k), d2.get(k)
        if isinstance(v1, dict) and isinstance(v2, dict):
            if nested_diff := data_diff(v1, v2):
                diff[k] = nested_diff
        elif v1 != v2:
            diff[k] = (v1, v2)
    return diff


def print_diff_details(diff: dict) -> None:
    for key, value in diff.items():
        if isinstance(value, dict):
            print(f"{key}:")
            print_diff_details(value)
        elif isinstance(value, tuple):
            print(f"Diff found in {key}:")
            left, right = value
            if are_all_instances_of(left, right, type=list):
                for idx, (l, r) in enumerate(zip_longest(left, right, fillvalue=[])):
                    if are_all_instances_of(l, r, type=(dict, list)):
                        if diff := data_diff(l, r):
                            print(f"Index {idx}:")
                            print_diff_details(diff)
                    elif l != r:
                        print(f"Index {idx}: {l} != {r}")
            elif are_all_instances_of(left, right, type=dict):
                print_diff_details(data_diff(left, right))
            elif left != right:
                if are_all_instances_of(left, right, type=str):
                    diff = difflib.unified_diff(left.splitlines(), right.splitlines())
                    print("\n".join(diff))
                else:
                    print(f"{left} != {right}")


# Enums
class EnumStrAndReprMixin:
    def __str__(self):
        return self.name

    __repr__ = __str__


class Action(EnumStrAndReprMixin, Enum):
    GET_ABI = "getabi"
    GET_SOURCE_CODE = "getsourcecode"
    GET_CONTRACT_CREATION = "getcontractcreation"


class StateMutability(EnumStrAndReprMixin, Enum):
    PURE = "pure"
    VIEW = "view"
    NONPAYABLE = "nonpayable"
    PAYABLE = "payable"


# Mixins
class ABIType(EnumStrAndReprMixin, Enum):
    FUNCTION = "function"
    CONSTRUCTOR = "constructor"
    EVENT = "event"
    FALLBACK = "fallback"
    RECEIVE = "receive"


class SkipDefaultFieldsReprMixin:
    def __repr__(self) -> str:
        def condition(f):
            return f.repr and getattr(self, f.name) not in (f.default, "")

        def display(f):
            return f"{f.name}={getattr(self, f.name)}"

        node_repr = ", ".join(map(display, filter(condition, fields(self))))
        return f"{self.__class__.__name__}({node_repr})"


# Polygon API Request Response
@dataclass
class Fields:
    module: str
    action: str
    address: str
    apikey: str


@dataclass
class Response:
    status: str
    message: str
    result: str = field(repr=False)
    action: str

    def __post_init__(self):
        self.status == self.status == "1"
        if not self.status:  # time to panic!
            raise ValueError(f"PANIC: {self.result}")


# ABI specific
@dataclass
class ABI:
    methods: List[Method]


@dataclass(repr=False)
class Method(SkipDefaultFieldsReprMixin):
    type: ABIType
    inputs: Optional[list[Input]] = None  # optional for constructor
    name: Optional[str] = None
    outputs: Optional[list] = None
    stateMutability: Optional[StateMutability] = None
    anonymous: Optional[bool] = None  # only for events

    def __post_init__(self):
        self.type = ABIType[self.type.upper()]
        if (attr := self.stateMutability) is not None:
            self.stateMutability = StateMutability[attr.upper()]
        if self.inputs is not None:
            self.inputs = list(starmap(Input, self.inputs))


@dataclass(repr=False)
class Input(SkipDefaultFieldsReprMixin):
    # both elementary and complex types (uintX, enum, function, etc.)
    type: str
    name: Optional[str] = None
    # only for events
    indexed: Optional[bool] = field(repr=False, default=None)
    # only for functions
    components: Optional[list[Input]] = field(repr=False, default=None)
    internalType: Optional[str] = field(repr=False, default=None)
    baseType: Optional[str] = field(repr=False, default=None)


# Contract data specific
@dataclass
class Contract:
    data: list[ContractData]


@dataclass(repr=False)
class ContractData(SkipDefaultFieldsReprMixin):
    SourceCode: SourceCode = field(repr=False)
    ABI: Optional[ABI] = field(repr=False, default=None)
    ContractName: Optional[str] = None
    CompilerVersion: Optional[str] = field(repr=False, default=None)
    OptimizationUsed: Optional[bool] = field(repr=False, default=None)
    Runs: Optional[int] = field(repr=False, default=None)
    ConstructorArguments: Optional[str] = field(repr=False, default=None)
    EVMVersion: Optional[str] = field(repr=False, default=None)
    Library: Optional[str] = field(repr=False, default=None)
    LicenseType: Optional[str] = field(repr=False, default=None)
    Proxy: Optional[bool] = None
    Implementation: Optional[str] = field(repr=False, default=None)
    SwarmSource: Optional[str] = field(repr=False, default=None)
    SourceCodeHash: Optional[str] = field(repr=False, default=None)
    SourceCodeMetaData: Optional[str] = field(repr=False, default=None)
    AST: Optional[str] = field(repr=False, default=None)
    SourceList: Optional[list[str]] = field(repr=False, default=None)
    DeveloperDoc: Optional[str] = field(repr=False, default=None)
    UserDoc: Optional[str] = field(repr=False, default=None)

    def __post_init__(self):
        if self.OptimizationUsed is not None:
            self.OptimizationUsed = self.OptimizationUsed == "1"
        if self.Proxy is not None:
            self.Proxy = self.Proxy == "1"
        if self.Runs is not None:
            self.Runs == int(self.Runs)
        if self.ABI is not None:  # most to post_init ABI
            self.ABI = ABI(list(map_starmap(Method, json.loads(self.ABI))))
        code = clean_code(self.SourceCode)
        self.SourceCode = SourceCode(**json.loads(code))


@dataclass
class SourceCode(SkipDefaultFieldsReprMixin):
    language: str
    version: Optional[str] = field(repr=False, default=None)
    settings: Optional[dict] = field(repr=False, default=None)
    sources: Optional[list[Source]] = field(repr=False, default=None)

    def __post_init__(self):
        if self.sources is not None:
            self.sources = list(starmap(Source, self.sources.items()))


@dataclass
class Source:
    path: Union[str, Path]
    code: str = field(repr=False, init=False)
    node: dict = field(repr=False, init=False)
    imports: list[Imports] = field(init=False, repr=False)
    pragmas: list[Pragma] = field(init=False, repr=False)

    def pprint(self):
        pprint(self.node)

    def __init__(self, path: str, data: dict):
        self.path = Path(path)
        self.code = data["content"]
        node = parser.parse(self.code)
        obj = parser.objectify(node)
        self.node = dict(node)
        self.pragmas = list(map_starmap(Pragma, obj.pragmas))
        self.imports = list(map_starmap(Import, obj.imports))
        self.contracts = obj.contracts  # not included in asdict


@dataclass
class Import:
    path: Union[str, Path]
    type: str = "ImportDirective"
    symbolAliases: dict = field(default_factory=dict)
    unitAlias: Optional[dict] = None

    def __post_init__(self):
        if isinstance(self.path, str):
            self.path = Path(self.path)


@dataclass
class Pragma:
    name: str
    value: str
    type: str = "PragmaDirective"


@lru_cache()
def get_contract_data(*address: Address, action: Action) -> dict[Address, Response]:
    responses = {}
    for address in addresses:
        fields = Fields(API_MODULE, action.value, address, API_KEY)
        response = requests.get(f"{API_ENDPOINT}/", params=asdict(fields))
        responses[address] = Response(**response.json(), action=action)
        print(f"obtained {action} for {address}")
    return responses


def process_response(response: Response) -> Union[ABI, Contract]:
    if response.action == Action.GET_ABI:
        return ABI(list(map_starmap(Method, json.loads(response.result))))
    elif response.action == Action.GET_SOURCE_CODE:
        return Contract(list(map_starmap(ContractData, response.result)))
    raise ValueError(f"Incorrect response type: {response}")


def compare_abis(addresses: Iterable[Address]) -> None:
    responses = get_contract_data(*addresses, action=Action.GET_ABI)
    abis = list(map(process_response, responses.values()))
    if diff := data_diff(*map(asdict, abis)):
        print("Differences in ABIs found")
        print_diff_details(diff)


def compare_source_code(addresses: Iterable[Address]) -> None:
    responses = get_contract_data(*addresses, action=Action.GET_SOURCE_CODE)
    contracts = list(map(process_response, responses.values()))
    if diff := data_diff(*map(asdict, contracts)):
        print("Differences in SourceCode found")
        print_diff_details(diff)


if __name__ == "__main__":
    if not API_KEY:
        raise ValueError("'POLYGONSCAN_API_KEY' not found in env vars")
    addresses = CONTRACT_ADDRESSES
    compare_abis(addresses)
    compare_source_code(addresses)
