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

"""This package contains the rounds of FlowchartToFSMAbciApp."""

from enum import Enum
from typing import Dict, List, Optional, Set, Tuple

from packages.valory.skills.abstract_round_abci.base import (
    AbciApp,
    AbciAppTransitionFunction,
    AbstractRound,
    AppState,
    BaseSynchronizedData,
    DegenerateRound,
    EventToTimeout,
)

from packages.eightballer.skills.rysk_roller.payloads import (
    AnalyseDataPayload,
    CallExercisedPayload,
    CallExpiredPayload,
    CollectDataPayload,
    CollectPriceDataPayload,
    MultiplexerPayload,
    PutExercisedPayload,
    PutExpiredPayload,
    UnderAllocatedPayload,
)


class Event(Enum):
    """FlowchartToFSMAbciApp Events"""

    PUT_EXERCISED = "put_exercised"
    CALL_EXPIRED = "call_expired"
    NOT_DONE = "not_done"
    ERROR = "error"
    UNDER_ALLOCATED = "under_allocated"
    SWAP_FROM_USDC_TO_ETH = "swap_from_usdc_to_eth"
    CALL_EXERCISED = "call_exercised"
    SWAP_FROM_ETH_TO_USDC = "swap_from_eth_to_usdc"
    DONE = "done"
    PUT_EXPIRED = "put_expired"
    SELL_CALL_OPTION = "sell_call_option"
    SELL_PUT_OPTION = "sell_put_option"


class SynchronizedData(BaseSynchronizedData):
    """
    Class to represent the synchronized data.

    This data is replicated by the tendermint application.
    """


class AnalyseDataRound(AbstractRound):
    """AnalyseDataRound"""

    payload_class = AnalyseDataPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    # TODO: replace AbstractRound with one of CollectDifferentUntilAllRound,
    # CollectSameUntilAllRound, CollectSameUntilThresholdRound,
    # CollectDifferentUntilThresholdRound, OnlyKeeperSendsRound, VotingRound,
    # from packages/valory/skills/abstract_round_abci/base.py
    # or implement the methods

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""

    def check_payload(self, payload: AnalyseDataPayload) -> None:
        """Check payload."""

    def process_payload(self, payload: AnalyseDataPayload) -> None:
        """Process payload."""


class CallExercisedRound(AbstractRound):
    """CallExercisedRound"""

    payload_class = CallExercisedPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    # TODO: replace AbstractRound with one of CollectDifferentUntilAllRound,
    # CollectSameUntilAllRound, CollectSameUntilThresholdRound,
    # CollectDifferentUntilThresholdRound, OnlyKeeperSendsRound, VotingRound,
    # from packages/valory/skills/abstract_round_abci/base.py
    # or implement the methods

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""

    def check_payload(self, payload: CallExercisedPayload) -> None:
        """Check payload."""

    def process_payload(self, payload: CallExercisedPayload) -> None:
        """Process payload."""


class CallExpiredRound(AbstractRound):
    """CallExpiredRound"""

    payload_class = CallExpiredPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    # TODO: replace AbstractRound with one of CollectDifferentUntilAllRound,
    # CollectSameUntilAllRound, CollectSameUntilThresholdRound,
    # CollectDifferentUntilThresholdRound, OnlyKeeperSendsRound, VotingRound,
    # from packages/valory/skills/abstract_round_abci/base.py
    # or implement the methods

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""

    def check_payload(self, payload: CallExpiredPayload) -> None:
        """Check payload."""

    def process_payload(self, payload: CallExpiredPayload) -> None:
        """Process payload."""


class CollectPriceDataRound(AbstractRound):
    """CollectDataRound"""

    payload_class = CollectDataPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    # TODO: replace AbstractRound with one of CollectDifferentUntilAllRound,
    # CollectSameUntilAllRound, CollectSameUntilThresholdRound,
    # CollectDifferentUntilThresholdRound, OnlyKeeperSendsRound, VotingRound,
    # from packages/valory/skills/abstract_round_abci/base.py
    # or implement the methods

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""

    def check_payload(self, payload: CollectDataPayload) -> None:
        """Check payload."""

    def process_payload(self, payload: CollectDataPayload) -> None:
        """Process payload."""


class CollectDataRound(AbstractRound):
    """CollectDataRound"""

    payload_class = CollectDataPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    # TODO: replace AbstractRound with one of CollectDifferentUntilAllRound,
    # CollectSameUntilAllRound, CollectSameUntilThresholdRound,
    # CollectDifferentUntilThresholdRound, OnlyKeeperSendsRound, VotingRound,
    # from packages/valory/skills/abstract_round_abci/base.py
    # or implement the methods

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        return Done

    def check_payload(self, payload: CollectDataPayload) -> None:
        """Check payload."""

    def process_payload(self, payload: CollectDataPayload) -> None:
        """Process payload."""


class MultiplexerRound(AbstractRound):
    """MultiplexerRound"""

    payload_class = MultiplexerPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    # TODO: replace AbstractRound with one of CollectDifferentUntilAllRound,
    # CollectSameUntilAllRound, CollectSameUntilThresholdRound,
    # CollectDifferentUntilThresholdRound, OnlyKeeperSendsRound, VotingRound,
    # from packages/valory/skills/abstract_round_abci/base.py
    # or implement the methods

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""

    def check_payload(self, payload: MultiplexerPayload) -> None:
        """Check payload."""

    def process_payload(self, payload: MultiplexerPayload) -> None:
        """Process payload."""


class PutExercisedRound(AbstractRound):
    """PutExercisedRound"""

    payload_class = PutExercisedPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    # TODO: replace AbstractRound with one of CollectDifferentUntilAllRound,
    # CollectSameUntilAllRound, CollectSameUntilThresholdRound,
    # CollectDifferentUntilThresholdRound, OnlyKeeperSendsRound, VotingRound,
    # from packages/valory/skills/abstract_round_abci/base.py
    # or implement the methods

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""

    def check_payload(self, payload: PutExercisedPayload) -> None:
        """Check payload."""

    def process_payload(self, payload: PutExercisedPayload) -> None:
        """Process payload."""


class PutExpiredRound(AbstractRound):
    """PutExpiredRound"""

    payload_class = PutExpiredPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    # TODO: replace AbstractRound with one of CollectDifferentUntilAllRound,
    # CollectSameUntilAllRound, CollectSameUntilThresholdRound,
    # CollectDifferentUntilThresholdRound, OnlyKeeperSendsRound, VotingRound,
    # from packages/valory/skills/abstract_round_abci/base.py
    # or implement the methods

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""

    def check_payload(self, payload: PutExpiredPayload) -> None:
        """Check payload."""

    def process_payload(self, payload: PutExpiredPayload) -> None:
        """Process payload."""


class UnderAllocatedRound(AbstractRound):
    """UnderAllocatedRound"""

    payload_class = UnderAllocatedPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    # TODO: replace AbstractRound with one of CollectDifferentUntilAllRound,
    # CollectSameUntilAllRound, CollectSameUntilThresholdRound,
    # CollectDifferentUntilThresholdRound, OnlyKeeperSendsRound, VotingRound,
    # from packages/valory/skills/abstract_round_abci/base.py
    # or implement the methods

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""

    def check_payload(self, payload: UnderAllocatedPayload) -> None:
        """Check payload."""

    def process_payload(self, payload: UnderAllocatedPayload) -> None:
        """Process payload."""


class SellCallOptionRound(DegenerateRound):
    """SellCallOptionRound"""


class SellPutOptionRound(DegenerateRound):
    """SellPutOptionRound"""


class SwapFromETHtoUSDCRound(DegenerateRound):
    """SwapFromETHtoUSDCRound"""


class SwapFromUSDCtoETHRound(DegenerateRound):
    """SwapFromUSDCtoETHRound"""


class FlowchartToFSMAbciApp(AbciApp[Event]):
    """FlowchartToFSMAbciApp"""

    initial_round_cls: AppState = CollectDataRound
    initial_states: Set[AppState] = {CollectDataRound}
    transition_function: AbciAppTransitionFunction = {
        CollectDataRound: {
            Event.DONE: CollectPriceDataRound
        },
        CollectPriceDataRound: {
            Event.DONE: AnalyseDataRound
        },
        AnalyseDataRound: {
            Event.DONE: MultiplexerRound
        },
        MultiplexerRound: {
            Event.NOT_DONE: CollectDataRound,
            Event.ERROR: CollectDataRound,
            Event.PUT_EXPIRED: PutExpiredRound,
            Event.PUT_EXERCISED: PutExercisedRound,
            Event.CALL_EXPIRED: CallExpiredRound,
            Event.CALL_EXERCISED: CallExercisedRound,
            Event.UNDER_ALLOCATED: UnderAllocatedRound,
            Event.SELL_PUT_OPTION: SellPutOptionRound,
            Event.SELL_CALL_OPTION: SellCallOptionRound
        },
        PutExpiredRound: {
            Event.SELL_PUT_OPTION: SellPutOptionRound
        },
        CallExpiredRound: {
            Event.SELL_CALL_OPTION: SellCallOptionRound
        },
        PutExercisedRound: {
            Event.SWAP_FROM_USDC_TO_ETH: SwapFromUSDCtoETHRound
        },
        CallExercisedRound: {
            Event.SWAP_FROM_ETH_TO_USDC: SwapFromETHtoUSDCRound
        },
        UnderAllocatedRound: {
            Event.SELL_PUT_OPTION: SellPutOptionRound,
            Event.SELL_CALL_OPTION: SellCallOptionRound
        },
        SellCallOptionRound: {},
        SwapFromUSDCtoETHRound: {},
        SwapFromETHtoUSDCRound: {},
        SellPutOptionRound: {}
    }
    final_states: Set[AppState] = {SwapFromUSDCtoETHRound, SellPutOptionRound, SellCallOptionRound, SwapFromETHtoUSDCRound}
    event_to_timeout: EventToTimeout = {}
    cross_period_persisted_keys: Set[str] = []
    db_pre_conditions: Dict[AppState, Set[str]] = {
        CollectDataRound: [],
    }
    db_post_conditions: Dict[AppState, Set[str]] = {
        SwapFromUSDCtoETHRound: [],
    	SellPutOptionRound: [],
    	SellCallOptionRound: [],
    	SwapFromETHtoUSDCRound: [],
    }
