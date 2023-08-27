from dataclasses import astuple
from pathlib import Path
from typing import Dict
from unittest import mock

import pytest
import web3 as w3
from aea.contracts.base import Contract
from aea.test_tools.test_contract import BaseContractTestCase
from aea_ledger_ethereum import EthereumApi, EthereumCrypto

from packages.zarathustra.contracts.homm_vault.contract import (
    HOMMVaultContract, OptionSeries, RequestQuoteOptionPrice)

NULL = "0x" + "0" * 40
DEFAULT_GAS = 1000000
DEFAULT_MAX_FEE_PER_GAS = 10**15
DEFAULT_MAX_PRIORITY_FEE_PER_GAS = 10**15
PACKAGE_DIR = Path(__file__).parent.parent


def test_dataclass_conversion():

    expected = ((1, 2, True, NULL, NULL, NULL), 3, False, 4)
    option_series = OptionSeries(
        expiration=1,
        strike=2,
        is_put=True,
        underlying=NULL,
        strike_asset=NULL,
        collateral=NULL,
    )
    request_params = RequestQuoteOptionPrice(
        option_series,
        _amount=3,
        is_sell=False,
        net_dhv_exposure=4,
    )
    assert astuple(request_params) == expected


class TestHOMMVaultContract(BaseContractTestCase):
    """Test HOMMVaultContract"""

    path_to_contract = PACKAGE_DIR
    contract: HOMMVaultContract
    ledger_identifier = EthereumCrypto.identifier

    @classmethod
    def finish_contract_deployment(cls) -> str:
        """Finish the contract deployment."""
        return NULL

    @classmethod
    def _deploy_contract(
        cls,
        contract: Contract,
        ledger_api: EthereumApi,
        deployer_crypto: EthereumCrypto,
        gas: int,
    ) -> Dict:
        """Deploy contract."""
        return {}

    def test_non_implemented_methods(
        self,
    ) -> None:
        """Test not implemented methods."""

        with pytest.raises(NotImplementedError):
            self.contract.get_raw_transaction(self.ledger_api, "")

        with pytest.raises(NotImplementedError):
            self.contract.get_raw_message(self.ledger_api, "")

        with pytest.raises(NotImplementedError):
            self.contract.get_state(self.ledger_api, "")

    def test_deposit(self):

        with mock.patch.object(w3.manager, "request_blocking"):
            result = self.contract.is_locked(
                ledger_api=self.ledger_api,
                contract=self.contract_address,
            )
            assert isinstance(result, bool)
