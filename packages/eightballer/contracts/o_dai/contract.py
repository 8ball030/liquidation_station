# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2023 eightballer
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

from typing import Any

from aea.common import JSONLike
from packages.eightballer.contracts.o_dai import PUBLIC_ID
from aea.contracts.base import Contract
from aea.crypto.base import LedgerApi, Address


class ODai(Contract):
    """The scaffold contract class for a smart contract."""

    contract_id = PUBLIC_ID

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
    def accrual_block_timestamp(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'accrual_block_timestamp' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.accrualBlockTimestamp().call()
        return {
            'int': result
        }



    @classmethod
    def admin(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'admin' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.admin().call()
        return {
            'address': result
        }



    @classmethod
    def allowance(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        owner: Address,
        spender: Address
        ) -> JSONLike:
        """Handler method for the 'allowance' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.allowance(owner=owner,
        spender=spender).call()
        return {
            'int': result
        }



    @classmethod
    def balance_of(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        owner: Address
        ) -> JSONLike:
        """Handler method for the 'balance_of' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.balanceOf(owner=owner).call()
        return {
            'int': result
        }



    @classmethod
    def borrow_balance_stored(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        account: Address
        ) -> JSONLike:
        """Handler method for the 'borrow_balance_stored' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.borrowBalanceStored(account=account).call()
        return {
            'int': result
        }



    @classmethod
    def borrow_index(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'borrow_index' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.borrowIndex().call()
        return {
            'int': result
        }



    @classmethod
    def borrow_rate_per_timestamp(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'borrow_rate_per_timestamp' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.borrowRatePerTimestamp().call()
        return {
            'int': result
        }



    @classmethod
    def comptroller(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'comptroller' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.comptroller().call()
        return {
            'address': result
        }



    @classmethod
    def decimals(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'decimals' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.decimals().call()
        return {
            'int': result
        }



    @classmethod
    def exchange_rate_stored(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'exchange_rate_stored' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.exchangeRateStored().call()
        return {
            'int': result
        }



    @classmethod
    def get_account_snapshot(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        account: Address
        ) -> JSONLike:
        """Handler method for the 'get_account_snapshot' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.getAccountSnapshot(account=account).call()
        return {
            'int': result,
        'int': result,
        'int': result,
        'int': result
        }



    @classmethod
    def get_cash(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'get_cash' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.getCash().call()
        return {
            'int': result
        }



    @classmethod
    def interest_rate_model(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'interest_rate_model' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.interestRateModel().call()
        return {
            'address': result
        }



    @classmethod
    def is_init(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'is_init' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.isInit().call()
        return {
            'bool': result
        }



    @classmethod
    def is_o_token(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'is_o_token' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.isOToken().call()
        return {
            'bool': result
        }



    @classmethod
    def name(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'name' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.name().call()
        return {
            'str': result
        }



    @classmethod
    def pending_admin(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'pending_admin' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.pendingAdmin().call()
        return {
            'address': result
        }



    @classmethod
    def protocol_seize_share_mantissa(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'protocol_seize_share_mantissa' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.protocolSeizeShareMantissa().call()
        return {
            'int': result
        }



    @classmethod
    def reserve_factor_mantissa(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'reserve_factor_mantissa' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.reserveFactorMantissa().call()
        return {
            'int': result
        }



    @classmethod
    def supply_rate_per_timestamp(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'supply_rate_per_timestamp' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.supplyRatePerTimestamp().call()
        return {
            'int': result
        }



    @classmethod
    def symbol(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'symbol' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.symbol().call()
        return {
            'str': result
        }



    @classmethod
    def total_borrows(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'total_borrows' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.totalBorrows().call()
        return {
            'int': result
        }



    @classmethod
    def total_reserves(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'total_reserves' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.totalReserves().call()
        return {
            'int': result
        }



    @classmethod
    def total_supply(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'total_supply' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.totalSupply().call()
        return {
            'int': result
        }



    @classmethod
    def accrual_block_timestamp(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'accrual_block_timestamp' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.accrualBlockTimestamp().call()
        return {
            'int': result
        }



    @classmethod
    def admin(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'admin' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.admin().call()
        return {
            'address': result
        }



    @classmethod
    def allowance(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        owner: Address,
        spender: Address
        ) -> JSONLike:
        """Handler method for the 'allowance' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.allowance(owner=owner,
        spender=spender).call()
        return {
            'int': result
        }



    @classmethod
    def balance_of(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        owner: Address
        ) -> JSONLike:
        """Handler method for the 'balance_of' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.balanceOf(owner=owner).call()
        return {
            'int': result
        }



    @classmethod
    def borrow_balance_stored(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        account: Address
        ) -> JSONLike:
        """Handler method for the 'borrow_balance_stored' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.borrowBalanceStored(account=account).call()
        return {
            'int': result
        }



    @classmethod
    def borrow_index(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'borrow_index' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.borrowIndex().call()
        return {
            'int': result
        }



    @classmethod
    def borrow_rate_per_timestamp(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'borrow_rate_per_timestamp' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.borrowRatePerTimestamp().call()
        return {
            'int': result
        }



    @classmethod
    def comptroller(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'comptroller' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.comptroller().call()
        return {
            'address': result
        }



    @classmethod
    def decimals(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'decimals' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.decimals().call()
        return {
            'int': result
        }



    @classmethod
    def exchange_rate_stored(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'exchange_rate_stored' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.exchangeRateStored().call()
        return {
            'int': result
        }



    @classmethod
    def get_account_snapshot(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        account: Address
        ) -> JSONLike:
        """Handler method for the 'get_account_snapshot' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.getAccountSnapshot(account=account).call()
        return {
            'int': result,
        'int': result,
        'int': result,
        'int': result
        }



    @classmethod
    def get_cash(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'get_cash' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.getCash().call()
        return {
            'int': result
        }



    @classmethod
    def interest_rate_model(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'interest_rate_model' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.interestRateModel().call()
        return {
            'address': result
        }



    @classmethod
    def is_init(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'is_init' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.isInit().call()
        return {
            'bool': result
        }



    @classmethod
    def is_o_token(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'is_o_token' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.isOToken().call()
        return {
            'bool': result
        }



    @classmethod
    def name(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'name' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.name().call()
        return {
            'str': result
        }



    @classmethod
    def pending_admin(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'pending_admin' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.pendingAdmin().call()
        return {
            'address': result
        }



    @classmethod
    def protocol_seize_share_mantissa(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'protocol_seize_share_mantissa' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.protocolSeizeShareMantissa().call()
        return {
            'int': result
        }



    @classmethod
    def reserve_factor_mantissa(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'reserve_factor_mantissa' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.reserveFactorMantissa().call()
        return {
            'int': result
        }



    @classmethod
    def supply_rate_per_timestamp(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'supply_rate_per_timestamp' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.supplyRatePerTimestamp().call()
        return {
            'int': result
        }



    @classmethod
    def symbol(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'symbol' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.symbol().call()
        return {
            'str': result
        }



    @classmethod
    def total_borrows(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'total_borrows' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.totalBorrows().call()
        return {
            'int': result
        }



    @classmethod
    def total_reserves(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'total_reserves' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.totalReserves().call()
        return {
            'int': result
        }



    @classmethod
    def total_supply(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'total_supply' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.totalSupply().call()
        return {
            'int': result
        }



    @classmethod
    def underlying(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        
        ) -> JSONLike:
        """Handler method for the 'underlying' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.underlying().call()
        return {
            'address': result
        }

