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

"""This module contains the scaffold contract definition."""
import logging
from collections import namedtuple
from enum import IntEnum, auto
from typing import Any, NamedTuple

from aea.common import JSONLike
from aea.configurations.base import PublicId
from aea.contracts.base import Contract
from aea.crypto.base import LedgerApi


class Error(IntEnum):
    def _generate_next_value_(name, start, count, last_values):
        """Generate consecutive automatic numbers starting from zero"""
        return count

    NO_ERROR = auto()
    UNAUTHORIZED = auto()
    COMPTROLLER_MISMATCH = auto()
    INSUFFICIENT_SHORTFALL = auto()
    INSUFFICIENT_LIQUIDITY = auto()
    INVALID_CLOSE_FACTOR = auto()
    INVALID_COLLATERAL_FACTOR = auto()
    INVALID_LIQUIDATION_INCENTIVE = auto()
    MARKET_NOT_ENTERED = auto()  # no longer possible
    MARKET_NOT_LISTED = auto()
    MARKET_ALREADY_LISTED = auto()
    MATH_ERROR = auto()
    NONZERO_BORROW_BALANCE = auto()
    PRICE_ERROR = auto()
    REJECTION = auto()
    SNAPSHOT_ERROR = auto()
    TOO_MANY_ASSETS = auto()
    TOO_MUCH_REPAY = auto()


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
        del ledger_api, contract, kwargs

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
        del ledger_api, contract, kwargs

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
        del ledger_api, contract, kwargs

    def get_account_liquidity(self, account: Address) -> NamedTuple:
        """Determine the current account liquidity wrt collateral requirements."""

        result = contract_interface.functions.getAccountLiquidity(account).call()

        error_code, liquidity, shortfall = result
        return to_named_tuple(
            error_code,
            liquidity=liquidity,
            shortfall=shortfall,
        )

    def liquidate_borrow_allowed(
        self,
        o_token_borrowed: Address,
        o_token_collateral: Address,
        liquidator: Address,
        borrower: Address,
        repay_amount: Wei,
    ) -> NamedTuple:
        """Checks if the liquidation should be allowed to occur."""

        contract_interface = cls.get_instance(
            ledger_api=ledger_api,
            contract_address=contract_address,
        )

        error_code = contract_interface.functions.liquidateBorrowAllowed(
            o_token_borrowed,
            o_token_collateral,
            liquidator,
            borrower,
            repay_amount,
        ).call()

        return to_named_tuple(error_code)

    def liquidate_calculate_seize_tokens(
        self,
        o_token_borrowed: Address,
        o_token_collateral: Address,
        actual_borrow_amount: Wei,
    ):
        """Calculate number of tokens of collateral asset to seize given an underlying amount.

        1. Read oracle prices for borrowed and collateral markets
        2. Get the exchange rate and calculate the number of collateral tokens to seize:
           seizeAmount = actualRepayAmount * liquidationIncentive * priceBorrowed / priceCollateral
           seizeTokens = seizeAmount / exchangeRate

        returns: number of oTokenCollateral tokens to be seized in a liquidation.
        """

        result = contract_interface.functions.liquidateCalculateSeizeTokens(
            o_token_borrowed,
            o_token_collateral,
            actual_borrow_amount,
        ).call()

        error_code, seize_tokens = result
        return to_named_tuple(error_code, seize_tokens=seize_tokens)

        ### Likely not relevant to us now:
        # seizeAllowed: Checks if the seizing of assets should be allowed to occur
        # seizeVerify: Validates seize and reverts on rejection.
