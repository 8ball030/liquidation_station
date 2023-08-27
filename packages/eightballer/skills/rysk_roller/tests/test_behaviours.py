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

"""This package contains round behaviours of FlowchartToFSMAbciApp."""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Hashable, Optional, Type

import pytest

from packages.eightballer.skills.rysk_roller.behaviours import (
    AnalyseDataBehaviour,
    CallExercisedBehaviour,
    CallExpiredBehaviour,
    CollectDataBehaviour,
    FlowchartToFSMRoundBehaviour,
    MultiplexerBehaviour,
    PutExercisedBehaviour,
    PutExpiredBehaviour,
    RyskRollerBaseBehaviour,
    UnderAllocatedBehaviour,
)
from packages.eightballer.skills.rysk_roller.rounds import (
    AnalyseDataRound,
    CallExercisedRound,
    CallExpiredRound,
    CollectDataRound,
    DegenerateRound,
    Event,
    FlowchartToFSMAbciApp,
    MultiplexerRound,
    PutExercisedRound,
    PutExpiredRound,
    SellCallOptionRound,
    SellPutOptionRound,
    SwapFromETHtoUSDCRound,
    SwapFromUSDCtoETHRound,
    SynchronizedData,
    UnderAllocatedRound,
)
from packages.valory.skills.abstract_round_abci.base import AbciAppDB
from packages.valory.skills.abstract_round_abci.behaviours import (
    AbstractRoundBehaviour,
    BaseBehaviour,
    make_degenerate_behaviour,
)
from packages.valory.skills.abstract_round_abci.test_tools.base import (
    FSMBehaviourBaseCase,
)


@dataclass
class BehaviourTestCase:
    """BehaviourTestCase"""

    name: str
    initial_data: Dict[str, Hashable]
    event: Event
    kwargs: Dict[str, Any] = field(default_factory=dict)


class BaseFlowchartToFSMTest(FSMBehaviourBaseCase):
    """Base test case."""

    path_to_skill = Path(__file__).parent.parent

    behaviour: FlowchartToFSMRoundBehaviour
    behaviour_class: Type[RyskRollerBaseBehaviour]
    next_behaviour_class: Type[RyskRollerBaseBehaviour]
    synchronized_data: SynchronizedData
    done_event = Event.DONE

    @property
    def current_behaviour_id(self) -> str:
        """Current RoundBehaviour's behaviour id"""

        return self.behaviour.current_behaviour.behaviour_id

    def fast_forward(self, data: Optional[Dict[str, Any]] = None) -> None:
        """Fast-forward on initialization"""

        data = data if data is not None else {}
        self.fast_forward_to_behaviour(
            self.behaviour,
            self.behaviour_class.behaviour_id,
            SynchronizedData(AbciAppDB(setup_data=AbciAppDB.data_to_lists(data))),
        )
        assert self.current_behaviour_id == self.behaviour_class.behaviour_id

    def complete(self, event: Event) -> None:
        """Complete test"""

        self.behaviour.act_wrapper()
        self.mock_a2a_transaction()
        self._test_done_flag_set()
        self.end_round(done_event=event)
        assert self.current_behaviour_id == self.next_behaviour_class.behaviour_id


class TestAnalyseDataBehaviour(BaseFlowchartToFSMTest):
    """Tests AnalyseDataBehaviour"""

    # TODO: set next_behaviour_class
    behaviour_class: Type[BaseBehaviour] = AnalyseDataBehaviour
    next_behaviour_class: Type[BaseBehaviour] = ...

    # TODO: provide test cases
    @pytest.mark.parametrize("test_case", [])
    def test_run(self, test_case: BehaviourTestCase) -> None:
        """Run tests."""

        self.fast_forward(test_case.initial_data)
        # TODO: mock the necessary calls
        # self.mock_ ...
        self.complete(test_case.event)


class TestCallExercisedBehaviour(BaseFlowchartToFSMTest):
    """Tests CallExercisedBehaviour"""

    # TODO: set next_behaviour_class
    behaviour_class: Type[BaseBehaviour] = CallExercisedBehaviour
    next_behaviour_class: Type[BaseBehaviour] = ...

    # TODO: provide test cases
    @pytest.mark.parametrize("test_case", [])
    def test_run(self, test_case: BehaviourTestCase) -> None:
        """Run tests."""

        self.fast_forward(test_case.initial_data)
        # TODO: mock the necessary calls
        # self.mock_ ...
        self.complete(test_case.event)


class TestCallExpiredBehaviour(BaseFlowchartToFSMTest):
    """Tests CallExpiredBehaviour"""

    # TODO: set next_behaviour_class
    behaviour_class: Type[BaseBehaviour] = CallExpiredBehaviour
    next_behaviour_class: Type[BaseBehaviour] = ...

    # TODO: provide test cases
    @pytest.mark.parametrize("test_case", [])
    def test_run(self, test_case: BehaviourTestCase) -> None:
        """Run tests."""

        self.fast_forward(test_case.initial_data)
        # TODO: mock the necessary calls
        # self.mock_ ...
        self.complete(test_case.event)


class TestCollectDataBehaviour(BaseFlowchartToFSMTest):
    """Tests CollectDataBehaviour"""

    # TODO: set next_behaviour_class
    behaviour_class: Type[BaseBehaviour] = CollectDataBehaviour
    next_behaviour_class: Type[BaseBehaviour] = ...

    # TODO: provide test cases
    @pytest.mark.parametrize("test_case", [])
    def test_run(self, test_case: BehaviourTestCase) -> None:
        """Run tests."""

        self.fast_forward(test_case.initial_data)
        # TODO: mock the necessary calls
        # self.mock_ ...
        self.complete(test_case.event)


class TestMultiplexerBehaviour(BaseFlowchartToFSMTest):
    """Tests MultiplexerBehaviour"""

    # TODO: set next_behaviour_class
    behaviour_class: Type[BaseBehaviour] = MultiplexerBehaviour
    next_behaviour_class: Type[BaseBehaviour] = ...

    # TODO: provide test cases
    @pytest.mark.parametrize("test_case", [])
    def test_run(self, test_case: BehaviourTestCase) -> None:
        """Run tests."""

        self.fast_forward(test_case.initial_data)
        # TODO: mock the necessary calls
        # self.mock_ ...
        self.complete(test_case.event)


class TestPutExercisedBehaviour(BaseFlowchartToFSMTest):
    """Tests PutExercisedBehaviour"""

    # TODO: set next_behaviour_class
    behaviour_class: Type[BaseBehaviour] = PutExercisedBehaviour
    next_behaviour_class: Type[BaseBehaviour] = ...

    # TODO: provide test cases
    @pytest.mark.parametrize("test_case", [])
    def test_run(self, test_case: BehaviourTestCase) -> None:
        """Run tests."""

        self.fast_forward(test_case.initial_data)
        # TODO: mock the necessary calls
        # self.mock_ ...
        self.complete(test_case.event)


class TestPutExpiredBehaviour(BaseFlowchartToFSMTest):
    """Tests PutExpiredBehaviour"""

    # TODO: set next_behaviour_class
    behaviour_class: Type[BaseBehaviour] = PutExpiredBehaviour
    next_behaviour_class: Type[BaseBehaviour] = ...

    # TODO: provide test cases
    @pytest.mark.parametrize("test_case", [])
    def test_run(self, test_case: BehaviourTestCase) -> None:
        """Run tests."""

        self.fast_forward(test_case.initial_data)
        # TODO: mock the necessary calls
        # self.mock_ ...
        self.complete(test_case.event)


class TestUnderAllocatedBehaviour(BaseFlowchartToFSMTest):
    """Tests UnderAllocatedBehaviour"""

    # TODO: set next_behaviour_class
    behaviour_class: Type[BaseBehaviour] = UnderAllocatedBehaviour
    next_behaviour_class: Type[BaseBehaviour] = ...

    # TODO: provide test cases
    @pytest.mark.parametrize("test_case", [])
    def test_run(self, test_case: BehaviourTestCase) -> None:
        """Run tests."""

        self.fast_forward(test_case.initial_data)
        # TODO: mock the necessary calls
        # self.mock_ ...
        self.complete(test_case.event)
