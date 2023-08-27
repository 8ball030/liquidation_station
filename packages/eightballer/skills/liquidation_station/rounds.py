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

"""This package contains the rounds of LiquidationStationAbciApp."""

from enum import Enum
from typing import Dict, List, Optional, Set, Tuple

from packages.eightballer.skills.liquidation_station.payloads import (
    CalculatePositionHealthPayload,
    CollectPositionsPayload,
    PrepareLiquidationTransactionsPayload,
    RegistrationPayload,
    ResetAndPausePayload,
    SubmitPositionLiquidationTransactionsPayload,
)
from packages.valory.skills.abstract_round_abci.base import (
    AbciApp,
    AbciAppTransitionFunction,
    AbstractRound,
    AppState,
    BaseSynchronizedData,
    DegenerateRound,
    EventToTimeout,
)


class Event(Enum):
    """LiquidationStationAbciApp Events"""

    NOT_TRIGGERED = "not_triggered"
    ROUND_TIMEOUT = "round_timeout"
    DONE = "done"
    NO_MAJORITY = "no_majority"
    RESET_TIMEOUT = "reset_timeout"


class SynchronizedData(BaseSynchronizedData):
    """
    Class to represent the synchronized data.

    This data is replicated by the tendermint application.
    """


class CalculatePositionHealthRound(AbstractRound):
    """CalculatePositionHealthRound"""

    payload_class = CalculatePositionHealthPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    # TODO: replace AbstractRound with one of CollectDifferentUntilAllRound,
    # CollectSameUntilAllRound, CollectSameUntilThresholdRound,
    # CollectDifferentUntilThresholdRound, OnlyKeeperSendsRound, VotingRound,
    # from packages/valory/skills/abstract_round_abci/base.py
    # or implement the methods

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        synchronized_data = self.synchronized_data
        return synchronized_data, Event.DONE

    def check_payload(self, payload: CalculatePositionHealthPayload) -> None:
        """Check payload."""

    def process_payload(self, payload: CalculatePositionHealthPayload) -> None:
        """Process payload."""


class CollectPositionsRound(AbstractRound):
    """CollectPositionsRound"""

    payload_class = CollectPositionsPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    # TODO: replace AbstractRound with one of CollectDifferentUntilAllRound,
    # CollectSameUntilAllRound, CollectSameUntilThresholdRound,
    # CollectDifferentUntilThresholdRound, OnlyKeeperSendsRound, VotingRound,
    # from packages/valory/skills/abstract_round_abci/base.py
    # or implement the methods

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        synchronized_data = self.synchronized_data
        return synchronized_data, Event.DONE

    def check_payload(self, payload: CollectPositionsPayload) -> None:
        """Check payload."""

    def process_payload(self, payload: CollectPositionsPayload) -> None:
        """Process payload."""


class PrepareLiquidationTransactionsRound(AbstractRound):
    """PrepareLiquidationTransactionsRound"""

    payload_class = PrepareLiquidationTransactionsPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    # TODO: replace AbstractRound with one of CollectDifferentUntilAllRound,
    # CollectSameUntilAllRound, CollectSameUntilThresholdRound,
    # CollectDifferentUntilThresholdRound, OnlyKeeperSendsRound, VotingRound,
    # from packages/valory/skills/abstract_round_abci/base.py
    # or implement the methods

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        synchronized_data = self.synchronized_data
        return synchronized_data, Event.DONE

    def check_payload(self, payload: PrepareLiquidationTransactionsPayload) -> None:
        """Check payload."""

    def process_payload(self, payload: PrepareLiquidationTransactionsPayload) -> None:
        """Process payload."""


class RegistrationRound(AbstractRound):
    """RegistrationRound"""

    payload_class = RegistrationPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    # TODO: replace AbstractRound with one of CollectDifferentUntilAllRound,
    # CollectSameUntilAllRound, CollectSameUntilThresholdRound,
    # CollectDifferentUntilThresholdRound, OnlyKeeperSendsRound, VotingRound,
    # from packages/valory/skills/abstract_round_abci/base.py
    # or implement the methods

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        synchronized_data = self.synchronized_data
        return synchronized_data, Event.DONE

    def check_payload(self, payload: RegistrationPayload) -> None:
        """Check payload."""

    def process_payload(self, payload: RegistrationPayload) -> None:
        """Process payload."""


class ResetAndPauseRound(AbstractRound):
    """ResetAndPauseRound"""

    payload_class = ResetAndPausePayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    # TODO: replace AbstractRound with one of CollectDifferentUntilAllRound,
    # CollectSameUntilAllRound, CollectSameUntilThresholdRound,
    # CollectDifferentUntilThresholdRound, OnlyKeeperSendsRound, VotingRound,
    # from packages/valory/skills/abstract_round_abci/base.py
    # or implement the methods

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        synchronized_data = self.synchronized_data
        return synchronized_data, Event.DONE

    def check_payload(self, payload: ResetAndPausePayload) -> None:
        """Check payload."""

    def process_payload(self, payload: ResetAndPausePayload) -> None:
        """Process payload."""


class SubmitPositionLiquidationTransactionsRound(AbstractRound):
    """SubmitPositionLiquidationTransactionsRound"""

    payload_class = SubmitPositionLiquidationTransactionsPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    # TODO: replace AbstractRound with one of CollectDifferentUntilAllRound,
    # CollectSameUntilAllRound, CollectSameUntilThresholdRound,
    # CollectDifferentUntilThresholdRound, OnlyKeeperSendsRound, VotingRound,
    # from packages/valory/skills/abstract_round_abci/base.py
    # or implement the methods

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        synchronized_data = self.synchronized_data
        return synchronized_data, Event.DONE

    def check_payload(
        self, payload: SubmitPositionLiquidationTransactionsPayload
    ) -> None:
        """Check payload."""

    def process_payload(
        self, payload: SubmitPositionLiquidationTransactionsPayload
    ) -> None:
        """Process payload."""


class LiquidationStationAbciApp(AbciApp[Event]):
    """LiquidationStationAbciApp"""

    initial_round_cls: AppState = RegistrationRound
    initial_states: Set[AppState] = {RegistrationRound}
    transition_function: AbciAppTransitionFunction = {
        RegistrationRound: {Event.DONE: CollectPositionsRound},
        CollectPositionsRound: {
            Event.DONE: CalculatePositionHealthRound,
            Event.ROUND_TIMEOUT: ResetAndPauseRound,
            Event.NO_MAJORITY: ResetAndPauseRound,
        },
        CalculatePositionHealthRound: {
            Event.DONE: PrepareLiquidationTransactionsRound,
            Event.ROUND_TIMEOUT: ResetAndPauseRound,
            Event.NO_MAJORITY: ResetAndPauseRound,
        },
        PrepareLiquidationTransactionsRound: {
            Event.DONE: SubmitPositionLiquidationTransactionsRound,
            Event.ROUND_TIMEOUT: ResetAndPauseRound,
            Event.NO_MAJORITY: ResetAndPauseRound,
        },
        SubmitPositionLiquidationTransactionsRound: {
            Event.DONE: ResetAndPauseRound,
            Event.NOT_TRIGGERED: ResetAndPauseRound,
        },
        ResetAndPauseRound: {
            Event.DONE: CollectPositionsRound,
            Event.NO_MAJORITY: ResetAndPauseRound,
            Event.RESET_TIMEOUT: ResetAndPauseRound,
        },
    }
    final_states: Set[AppState] = set()
    event_to_timeout: EventToTimeout = {}
    cross_period_persisted_keys: Set[str] = []
    db_pre_conditions: Dict[AppState, Set[str]] = {
        RegistrationRound: [],
    }
    db_post_conditions: Dict[AppState, Set[str]] = {}
