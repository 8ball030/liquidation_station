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

from dataclasses import astuple, dataclass
from enum import Enum
from typing import Any, List

from aea.common import Address, JSONLike
from aea.configurations.base import PublicId
from aea.contracts.base import Contract
from aea.crypto.base import LedgerApi

Shares = Assets = int


class ActionType(Enum):
    """ActionType"""

    ISSUE = "issue"
    BUY_OPTION = "buy_option"
    SELL_OPTION = "sell_option"
    CLOSE_OPTION = "close_option"


class OperationType(Enum):
    """OperationType"""

    OPYN = "opyn"
    RYSK = "rysk"


@dataclass
class OptionSeries:
    """OptionSeries"""

    expiration: int
    strike: int
    is_put: bool
    underlying: Address
    strike_asset: Address
    collateral: Address


@dataclass
class ActionArgs:
    """ActionArgs"""

    action_type: ActionType
    second_address: Address
    asset: Address
    vault_id: int
    amount: int
    option_series: OptionSeries
    acceptable_premium: int
    data: bytes


@dataclass
class OperationProcedure:
    """OperationProcedure"""

    operation: OperationType
    operation_queue: list[ActionArgs]


@dataclass
class RequestQuoteOptionPrice:
    """RequestQuoteOptionPrice"""

    _option_series: OptionSeries
    _amount: int
    is_sell: bool
    net_dhv_exposure: int


@dataclass
class QuoteOptionPrice:
    """QuoteOptionPrice"""

    total_premium: int
    total_delta: int
    total_fees: int


@dataclass
class Component:
    """Component"""

    epoch: int
    shares: int  # e18


@dataclass
class CompleteWithdrawal:
    """CompleteWithdrawal"""

    withdrawal_amount: int
    withdrawal_shares: int
    components: list[Component]


class HOMMVaultContract(Contract):
    """The Higher Order Market Maker Vault smart contract."""

    contract_id = PublicId.from_str("zarathustra/homm_vault:0.1.0")

    @classmethod
    def get_raw_transaction(
        cls, ledger_api: LedgerApi, contract_address: str, **kwargs: Any
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
        cls, ledger_api: LedgerApi, contract_address: str, **kwargs: Any
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
        cls, ledger_api: LedgerApi, contract_address: str, **kwargs: Any
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
    def deposit(
        cls,
        ledger_api: LedgerApi,
        contract: Address,
        assets: Assets,
        receiver: Address,
    ) -> Shares:
        """
        Deposit "assets" (USDC) into vault

        :param assets: amount of "assets" (USDC) to deposit.
        :param receiver: address to send "shares" (HOMM) to.
        :return: number of shares
        """

        contract_interface = cls.get_instance(
            ledger_api=ledger_api,
            contract_address=contract,
        )

        return contract_interface.functions.deposit(
            assets,
            receiver,
        )

    @classmethod
    def mint(
        cls,
        ledger_api: LedgerApi,
        contract: Address,
        shares: Shares,
        receiver: Address,
    ) -> Assets:
        """
        Mint "shares" Vault shares (HOMM) to "receiver" by depositing "assets" (USDC) of underlying tokens.

        :param shares: number of shares
        :param receiver: receiver address
        :return: amount of assets
        """

        contract_interface = cls.get_instance(
            ledger_api=ledger_api,
            contract_address=contract,
        )

        return contract_interface.functions.mint(
            shares,
            receiver,
        )

    @classmethod
    def withdraw(
        cls,
        ledger_api: LedgerApi,
        contract: Address,
        assets: Assets,
        receiver: Address,
        owner: Address,
    ) -> Shares:
        """
        Withdraw "asset" from vault.

        :param assets: amount of "asset" (USDC) to withdraw
        :param: receiver address to send "asset" (USDC) to
        :return: owner address of owner
        """

        contract_interface = cls.get_instance(
            ledger_api=ledger_api,
            contract_address=contract,
        )

        return contract_interface.functions.withdraw(
            assets,
            receiver,
            owner,
        )

    @classmethod
    def redeem(
        cls,
        ledger_api: LedgerApi,
        contract: Address,
        shares: Shares,
        receiver: Address,
        owner: Address,
    ) -> Assets:
        """
        Burn "shares" Vault shares (HOMM) from "owner" and sends "assets" (USDC) of underlying tokens to "receiver".

        :param shares: number of shares
        :param receiver: address of the receiver
        :param owner: address of the owner
        """

        contract_interface = cls.get_instance(
            ledger_api=ledger_api,
            contract_address=contract,
        )

        return contract_interface.functions.redeem(
            shares,
            receiver,
            owner,
        )

    @classmethod
    def total_assets(
        cls,
        ledger_api: LedgerApi,
        contract: Address,
    ) -> int:
        """Returns the total amount of "assets" (USDC) held by this contract.

        :return: int
        """

        contract_interface = cls.get_instance(
            ledger_api=ledger_api,
            contract_address=contract,
        )

        return contract_interface.functions.totalAssets().call()

    @classmethod
    def is_locked(
        cls,
        ledger_api: LedgerApi,
        contract: Address,
    ) -> bool:
        """Returns true if deposits/withdraws are locked.

        return: bool
        """

        contract_interface = cls.get_instance(
            ledger_api=ledger_api,
            contract_address=contract,
        )

        return contract_interface.functions.isLocked().call()

    # *´:°•.°+.*•´.*:˚.°*.˚•´.°:°•.°•.*•´.*:˚.°*.˚•´.°:°•.°+.*•´.*:* #
    # *                  FUND OPERATOR FUNCTIONS                   * #
    # *.•°:°.´+˚.*°.˚:*.´•*.+°.•°:´*.´•*.•°.•°:°.´:•˚°.*°.˚:*.´+°.•* #
    @classmethod
    def deposit_liquidity(
        cls,
        ledger_api: LedgerApi,
        contract: Address,
        _amount: int,
    ) -> bool:
        """
        Deposit liquidity into Rysk liquidity pool.

        :param _amount: amount of liquidity to deposit into Rysk Liq Pool
        :return: bool
        """
        contract_interface = cls.get_instance(
            ledger_api=ledger_api,
            contract_address=contract,
        )

        return contract_interface.functions.depositLiquidity(_amount).call()

    @classmethod
    def initiate_withdraw(
        cls,
        ledger_api: LedgerApi,
        contract: Address,
        _shares: Shares,
    ) -> None:
        """Generate Rysk withdrawal reciept for share amount operator input

        returns: None
        NOTE: Monitor via check withdraw request inside the liquidity pool.
        """
        contract_interface = cls.get_instance(
            ledger_api=ledger_api,
            contract_address=contract,
        )

        return contract_interface.functions.initiateWithdraw(_shares).call()

    @classmethod
    def complete_withdraw(
        cls,
        ledger_api: LedgerApi,
        contract: Address,
    ) -> CompleteWithdrawal:
        """
        Complete withdrawal from Rysk liquidity pool using existing receipt

        :return: None
        """

        contract_interface = cls.get_instance(
            ledger_api=ledger_api,
            contract_address=contract,
        )

        result = contract_interface.functions.completeWithdraw().call()
        return CompleteWithdrawal(*astuple(result))

    @classmethod
    def trade(
        cls,
        ledger_api: LedgerApi,
        contract: Address,
        operations_procedures: List[OperationProcedure],
    ) -> None:
        """
        Trade options on Rysk

        param: _operateProcedures array of operation procedures to execute on Rysk
        :return: None
        """

        contract_interface = cls.get_instance(
            ledger_api=ledger_api,
            contract_address=contract,
        )
        return contract_interface.functions.trade(operations_procedures).call()

    @classmethod
    def redeem_option_tokens(
        cls,
        ledger_api: LedgerApi,
        contract: Address,
        _series: Address,
    ) -> Assets:
        """
        Redeem option series on Rysk

        param: _series the address of the option token to be burnt and redeemed.
        :return: amount of assets
        """

        contract_interface = cls.get_instance(
            ledger_api=ledger_api,
            contract_address=contract,
        )

        return contract_interface.functions.redeemOptionTokens(_series).call()

    @classmethod
    def quote_option_price(
        cls,
        ledger_api: LedgerApi,
        contract: Address,
        request_quote_option_price: RequestQuoteOptionPrice,
    ) -> QuoteOptionPrice:
        """
        Get a quote for the option price from the BeyondPricer

        :param request_quote_option_price:
        :return: amount of assets
        """

        contract_interface = cls.get_instance(
            ledger_api=ledger_api,
            contract_address=contract,
        )

        result = contract_interface.functions.quoteOptionPrice(
            *astuple(request_quote_option_price)
        ).call()

        total_premium, total_delta, total_fees = result
        return QuoteOptionPrice(total_premium, total_delta, total_fees)

    @classmethod
    def get_call_slippage_gradient_multipliers(
        cls,
        ledger_api: LedgerApi,
        contract: Address,
        _series: Address,
    ) -> Assets:
        """getCallSlippageGradientMultipliers"""

        contract_interface = cls.get_instance(
            ledger_api=ledger_api,
            contract_address=contract,
        )

        return contract_interface.functions.getCallSlippageGradientMultipliers().call()

    @classmethod
    def get_put_slippage_gradient_multipliers(
        cls,
        ledger_api: LedgerApi,
        contract: Address,
        _series: Address,
    ) -> Assets:
        """getPutSlippageGradientMultipliers"""

        contract_interface = cls.get_instance(
            ledger_api=ledger_api,
            contract_address=contract,
        )

        return contract_interface.functions.getPutSlippageGradientMultipliers().call()
