# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2023 zarathustra
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

"""This module contains the Unitroller contract definition."""

import logging
from typing import Any, NamedTuple
from enum import IntEnum, auto
from collections import namedtuple

from aea.common import JSONLike
from aea.configurations.base import PublicId
from aea.contracts.base import Contract
from aea.crypto.base import LedgerApi

from packages.zarathustra.contracts import Error


Address = str
Wei = int

PUBLIC_ID = PublicId.from_str("zarathustra/unitroller:0.1.0")

_logger = logging.getLogger(
    f"aea.packages.{PUBLIC_ID.author}.contracts.{PUBLIC_ID.name}.contract"
)


def to_named_tuple(error: int, **kwargs) -> NamedTuple:
    kwargs = {"error": Error(error), **kwargs}
    keys, values = zip(*kwargs.items())
    return namedtuple("contract_response", keys)(*values)


@dataclass
class LiquidateBorrowAllowed:
    o_token_borrowed: Address
    o_token_collateral: Address
    liquidator: Address
    borrower: Address
    repay_amount: Wei


@dataclass
class LiquidateCalculateSeizeTokens:
    o_token_borrowed: Address
    o_token_collateral: Address
    actual_repay_amount: Wei


class Unitroller(Contract):
    """Unitroller.

    Storage for the comptroller is at this address,
    while execution is delegated to the comptrollerImplementation.
    """

    contract_id = PUBLIC_ID

    @classmethod
    def get_raw_transaction(
        cls, ledger_api: LedgerApi, contract: Address, **kwargs: Any
    ) -> JSONLike:
        """
        Handler method for the 'GET_RAW_TRANSACTION' requests.

        Implement this method in the sub class if you want
        to handle the contract requests manually.

        :param ledger_api: the ledger apis.
        :param contract_address: the contract address.
        :param kwargs: the keyword arguments.
        :return: the tx  # noqa: DAR202
        """
        raise NotImplementedError

    @classmethod
    def get_raw_message(
        cls, ledger_api: LedgerApi, contract: Address, **kwargs: Any
    ) -> bytes:
        """
        Handler method for the 'GET_RAW_MESSAGE' requests.

        Implement this method in the sub class if you want
        to handle the contract requests manually.

        :param ledger_api: the ledger apis.
        :param contract_address: the contract address.
        :param kwargs: the keyword arguments.
        :return: the tx  # noqa: DAR202
        """
        raise NotImplementedError

    @classmethod
    def get_state(
        cls, ledger_api: LedgerApi, contract: Address, **kwargs: Any
    ) -> JSONLike:
        """
        Handler method for the 'GET_STATE' requests.

        Implement this method in the sub class if you want
        to handle the contract requests manually.

        :param ledger_api: the ledger apis.
        :param contract_address: the contract address.
        :param kwargs: the keyword arguments.
        :return: the tx  # noqa: DAR202
        """
        raise NotImplementedError

    @classmethod
    def get_account_liquidity(
        cls, ledger_api: LedgerApi, contract_address: str, account: Address
    ) -> NamedTuple:
        """Determine the current account liquidity wrt collateral requirements."""

        contract = cls.get_instance(
            ledger_api=ledger_api,
            contract_address=contract_address,
        )

        result = contract.functions.getAccountLiquidity(account).call()
        error_code, liquidity, shortfall = result

        return to_named_tuple(
            error_code,
            liquidity=liquidity,
            shortfall=shortfall,
        )

    @classmethod
    def get_price_oracle(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> NamedTuple:
        """Get price oracle address."""

        contract = cls.get_instance(
            ledger_api=ledger_api,
            contract_address=contract_address,
        )

        return to_named_tuple(contract.functions.oracle().call())

    @classmethod
    def get_all_markets(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> list[Address]:
        """Get all oToken market addresses."""

        contract = cls.get_instance(
            ledger_api=ledger_api,
            contract_address=contract_address,
        )

        return contract.functions.getAllMarkets().call()

    @classmethod
    def liquidation_incentive_mantissa(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> int:
        """Get liquidation incentive mantissa.

        Represents the amount of discount a liquidator receives when they liquidate a borrower's collateral.
        """

        contract = cls.get_instance(
            ledger_api=ledger_api,
            contract_address=contract_address,
        )

        return contract.functions.liquidationIncentiveMantissa().call()

    @classmethod
    def liquidate_borrow_allowed(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        data: LiquidateBorrowAllowed,
    ) -> NamedTuple:
        """Checks if the liquidation should be allowed to occur."""

        contract = cls.get_instance(
            ledger_api=ledger_api,
            contract_address=contract_address,
        )

        error_code = contract.functions.liquidateBorrowAllowed(**asdict(data)).call()

        return to_named_tuple(error_code)

    @classmethod
    def liquidate_calculate_seize_tokens(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        data: LiquidateCalculateSeizeTokens,
    ):
        """Calculate number of tokens of collateral asset to seize given an underlying amount.

        1. Read oracle prices for borrowed and collateral markets
        2. Get the exchange rate and calculate the number of collateral tokens to seize:
           seizeAmount = actualRepayAmount * liquidationIncentive * priceBorrowed / priceCollateral
           seizeTokens = seizeAmount / exchangeRate

        returns: error code and number of oTokenCollateral tokens to be seized in a liquidation.
        """

        contract = cls.get_instance(
            ledger_api=ledger_api,
            contract_address=contract_address,
        )

        result = contract.functions.liquidateCalculateSeizeTokens(**asdict(data)).call()

        error_code, seize_tokens = result
        return to_named_tuple(error_code, seize_tokens=seize_tokens)

        # Likely not relevant to us now:
        # seizeAllowed: Checks if the seizing of assets should be allowed to occur
        # seizeVerify: Validates seize and reverts on rejection.
