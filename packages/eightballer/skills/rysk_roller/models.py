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

"""This module contains the shared state for the abci skill of FlowchartToFSMAbciApp."""

from enum import Enum

from packages.eightballer.skills.rysk_roller.rounds import \
    FlowchartToFSMAbciApp
from packages.valory.skills.abstract_round_abci.models import BaseParams
from packages.valory.skills.abstract_round_abci.models import \
    BenchmarkTool as BaseBenchmarkTool
from packages.valory.skills.abstract_round_abci.models import \
    Requests as BaseRequests
from packages.valory.skills.abstract_round_abci.models import \
    SharedState as BaseSharedState


class SharedState(BaseSharedState):
    """Keep the current shared state of the skill."""

    abci_app_cls = FlowchartToFSMAbciApp


class StrategyAction(Enum):
    """Strategy action."""

    SELL_CALL = 1
    SELL_PUT = 2
    SWAP_USDC_TO_ETH = 3
    SWAP_ETH_TO_USDC = 4
    HOLD = 5


Params = BaseParams
Requests = BaseRequests
BenchmarkTool = BaseBenchmarkTool
