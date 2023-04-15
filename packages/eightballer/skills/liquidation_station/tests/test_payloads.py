# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2023 Valory AG
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

"""This package contains payload tests for the LiquidationStationAbciApp."""

from typing import Type, Hashable
from dataclasses import dataclass

import pytest

from packages.eightballer.skills.liquidation_station.payloads import (
    BaseTxPayload,
    CalculatePositionHealthPayload,
    CollectPositionsPayload,
    PrepareLiquidationTransactionsPayload,
    RegistrationPayload,
    ResetAndPausePayload,
    SubmitPositionLiquidationTransactionsPayload,
)


@dataclass
class PayloadTestCase:
    """PayloadTestCase"""

    name: str
    payload_cls: Type[BaseTxPayload]
    content: Hashable


# TODO: provide test cases
@pytest.mark.parametrize("test_case", [])
def test_payloads(test_case: PayloadTestCase) -> None:
    """Tests for LiquidationStationAbciApp payloads"""

    payload = test_case.payload_cls(sender="sender", content=test_case.content)
    assert payload.sender == "sender"
    assert payload.from_json(payload.json) == payload

