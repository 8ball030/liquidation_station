
import os
import json
from web3 import Web3
from brownie import Contract, network
import subprocess
from pathlib import Path

AUTHOR = "zarathustra"
EXPECTED_ENV_VARS = [
    "WEB3_INFURA_PROJECT_ID",
    "POLYGONSCAN_TOKEN",
]

# mainnet addresses

ADDRESSES = dict(
    comptroller="0xf29d0ae1A29C453df338C5eEE4f010CFe08bb3FF",
    unitroller="0x8849f1a0cB6b5D6076aB150546EddEe193754F1C",
    oracle="0x421FF03Fe1085bce50ec5Bf06c5907119d87672F",
    jump_interest_model="0x15c7DAaD15E3EE00C30C16D6294ea3528641165a",
    o_matic_logic="0x188D24cfEB2837c11Fd22F1462C6E0174cD910Bc",
    o_matic="0xE554E874c9c60E45F1Debd479389C76230ae25A8",
    o_token_logic="0xb329FC9379dBf71BC58178383BA494D10D4E296F",
    o_wbtc="0x3B9128Ddd834cE06A60B0eC31CCfB11582d8ee18",
    o_dai="0x2175110F2936bf630a278660E9B6E4EFa358490A",
    o_weth="0xb2D9646A1394bf784E376612136B3686e74A325F",
    o_usdc="0xEBb865Bf286e6eA8aBf5ac97e1b56A76530F3fBe",
    o_usdt="0x1372c34acC14F1E8644C72Dad82E3a21C211729f",
    o_mai="0xC57E5e261d49Af3026446de3eC381172f17bB799",
    o_maticx="0xAAcc5108419Ae55Bc3588E759E28016d06ce5F40",
    
    ### NOTE: Contract source code not verified
    # oj_eur="0x29b0F07d5A61595685a17D5F9F86313742Ebd6Bc",
    # o_gdai="0x6F063Fe661d922e4fd77227f8579Cb84f9f41F0B",
    # ov_ghst="0xE053A4014b50666ED388ab8CbB18D5834de0aB12",
    # owst_eth="0xf06eda703c62b9889c75dccde927b93bde1ae654",
    # maximillion="0x3eA022fA3606fffF3eD522a87Bf45965F2dDD236",
)


network.connect("polygon-main")
cmd_template = "autonomy scaffold -tlr contract {name}"
destination = "packages {author} contracts {name}"


def check_env_for_keys() -> None:
    for env_var in EXPECTED_ENV_VARS:
        if not os.environ.get(env_var):
            raise EnvironmentError(f"{env_var} not found")


def define_contract_path(name: str) -> Path:
    parts = destination.format(author=AUTHOR, name=name).split()
    return Path(*parts).absolute()


def scaffold_contract(name: str) -> None:
    cmd = cmd_template.format(name=name)
    result = subprocess.run(
        cmd.split(),
        capture_output=True,
        encoding="utf-8",
    )
    if result.returncode != 0:
        raise subprocess.CalledProcessError(result.stderr)
    

def add_contract_abi(path: Path, address: str) -> None:
    contract = Contract.from_explorer(address)
    abi_path = path / "build"
    abi_path.mkdir()
    abi_file = abi_path / f"{name}.json"
    content = json.dumps(contract.abi, indent=4)
    abi_file.write_text(content)
    

def setup_contract(name: str, address: str) -> None:
    path = define_contract_path(name)
    if path.exists():
        print(f"contract already exists: {path}")
        return
    
    scaffold_contract(name)
    print(f"scaffolded contract at: {path}")

    add_contract_abi(path, address)
    print(f"dumped ABI: {name} - {address}")


if __name__ == "__main__":
    check_env_for_keys()
    for name, address in ADDRESSES.items():
        setup_contract(name, address)
