"""Test for contract module."""

from pathlib import Path
from dataclasses import dataclass, ascict

import pytest

from aea_test_autonomy.base_test_classes.contracts import BaseContractTest
from aea_test_autonomy.docker.base import skip_docker_tests

from packages.zarathustra.contracts import (
    OVIX_CONTRACT_ADDRESSES_POLYGON_POS,
    NULL_ADDRESS,
    Error,
)
from packages.zarathustra.contracts.unitroller.contract import (
    Unitroller,
    LiquidateBorrowAllowed,
    LiquidateCalculateSeizeTokens,
    to_named_tuple,
)

PACKAGE_DIR = Path(__file__).parent.parent

O_MATIC = OVIX_CONTRACT_ADDRESSES_POLYGON_POS.O_MATIC


@skip_docker_tests
class TestUnitroller(BaseContractTest):
    """Test Unitroller contract."""

    contract: Unitroller
    contract_address = OVIX_CONTRACT_ADDRESSES_POLYGON_POS.UNITROLLER
    contract_directory = PACKAGE_DIR

    def test_get_account_liquidity(self) -> None:
        """Test get token URI method."""

        contract_response = self.contract.get_account_liquidity(
            ledger_api=self.ledger_api,
            contract_address=self.contract_address,
            account=NULL_ADDRESS,
        )

        assert contract_response._fields == ("error", "liquidity", "shortfall")
        assert contract_response.error == Error.NO_ERROR
        assert contract_response.liquidity == 0
        assert contract_response.shortfall == 0

    def test_get_price_oracle(self) -> None:
        """Test get token URI method."""

        contract_response = self.contract.get_price_oracle(
            ledger_api=self.ledger_api,
            contract_address=self.contract_address,
        )

        assert isinstance(contract_response.price_oracle, str)
        assert int(contract_response.price_oracle, 16)

    def test_get_all_markets(self) -> None:
        """Test get token URI method."""

        contract_response = self.contract.get_all_markets(
            ledger_api=self.ledger_api,
            contract_address=self.contract_address,
        )

        assert isinstance(contract_response, list)

    @pytest.mark.parametrize(
        "test_case",
        [
            (LiquidateBorrowAllowed(*([NULL_ADDRESS] * 4), 0), Error.MARKET_NOT_LISTED),
        ],
    )
    def test_liquidate_borrow_allowed(
        self, test_case: LiquidateBorrowAllowed, expected: Error
    ) -> None:
        """Test get token URI method."""

        contract_response = self.contract.liquidate_borrow_allowed(
            ledger_api=self.ledger_api,
            contract_address=self.contract_address,
            data=test_case,
        )

        assert contract_response.error == expected

    @pytest.mark.parametrize(
        "test_case",
        [
            (LiquidateCalculateSeizeTokens(O_MATIC, O_MATIC, 0), to_named_tuple(0, 0)),
        ],
    )
    def test_liquidate_calculate_seize_tokens(
        self,
        test_case: LiquidateCalculateSeizeTokens,
        expected: NamedTuple,
    ) -> None:
        """Test get token URI method."""

        contract_response = self.contract.liquidate_calculate_seize_tokens(
            ledger_api=self.ledger_api,
            contract_address=self.contract_address,
            data=test_case,
        )

        assert contract_response == expected
