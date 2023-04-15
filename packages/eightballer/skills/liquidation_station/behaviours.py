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

"""This package contains round behaviours of LiquidationStationAbciApp."""

from abc import ABC
from typing import Generator, Set, Type, cast

from packages.valory.skills.abstract_round_abci.base import AbstractRound
from packages.valory.skills.abstract_round_abci.behaviours import (
    AbstractRoundBehaviour,
    BaseBehaviour,
)

from packages.eightballer.skills.liquidation_station.models import Params
from packages.eightballer.skills.liquidation_station.rounds import (
    SynchronizedData,
    LiquidationStationAbciApp,
    CalculatePositionHealthRound,
    CollectPositionsRound,
    PrepareLiquidationTransactionsRound,
    RegistrationRound,
    ResetAndPauseRound,
    SubmitPositionLiquidationTransactionsRound,
)
from packages.eightballer.skills.liquidation_station.rounds import (
    CalculatePositionHealthPayload,
    CollectPositionsPayload,
    PrepareLiquidationTransactionsPayload,
    RegistrationPayload,
    ResetAndPausePayload,
    SubmitPositionLiquidationTransactionsPayload,
)


class LiquidationStationBaseBehaviour(BaseBehaviour, ABC):
    """Base behaviour for the liquidation_station skill."""

    @property
    def synchronized_data(self) -> SynchronizedData:
        """Return the synchronized data."""
        return cast(SynchronizedData, super().synchronized_data)

    @property
    def params(self) -> Params:
        """Return the params."""
        return cast(Params, super().params)


class CalculatePositionHealthBehaviour(LiquidationStationBaseBehaviour):
    """CalculatePositionHealthBehaviour"""

    matching_round: Type[AbstractRound] = CalculatePositionHealthRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""
        self.context.logger.info("CalculatePositionHealthBehaviour: In the behaviour")

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = CalculatePositionHealthPayload(sender=sender, )

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()


class CollectPositionsBehaviour(LiquidationStationBaseBehaviour):
    """CollectPositionsBehaviour"""

    matching_round: Type[AbstractRound] = CollectPositionsRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""
        self.context.logger.info("CollectPositionsBehaviour: In the behaviour")

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = CollectPositionsPayload(sender=sender, )

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()


class PrepareLiquidationTransactionsBehaviour(LiquidationStationBaseBehaviour):
    """PrepareLiquidationTransactionsBehaviour"""

    matching_round: Type[AbstractRound] = PrepareLiquidationTransactionsRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""
        self.context.logger.info("PrepareLiquidationTransactionsBehaviour: In the behaviour")

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = PrepareLiquidationTransactionsPayload(sender=sender, )

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()


class RegistrationBehaviour(LiquidationStationBaseBehaviour):
    """RegistrationBehaviour"""

    matching_round: Type[AbstractRound] = RegistrationRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""
        self.context.logger.info("RegistrationBehaviour: In the behaviour")

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = RegistrationPayload(sender=sender, )

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()


class ResetAndPauseBehaviour(LiquidationStationBaseBehaviour):
    """ResetAndPauseBehaviour"""

    matching_round: Type[AbstractRound] = ResetAndPauseRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""
        self.context.logger.info("ResetAndPauseBehaviour: In the behaviour")

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = ResetAndPausePayload(sender=sender, )

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()


class SubmitPositionLiquidationTransactionsBehaviour(LiquidationStationBaseBehaviour):
    """SubmitPositionLiquidationTransactionsBehaviour"""

    matching_round: Type[AbstractRound] = SubmitPositionLiquidationTransactionsRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""
        self.context.logger.info("SubmitPositionLiquidationTransactionsBehaviour: In the behaviour")

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = SubmitPositionLiquidationTransactionsPayload(sender=sender, )

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()


class LiquidationStationRoundBehaviour(AbstractRoundBehaviour):
    """LiquidationStationRoundBehaviour"""

    initial_behaviour_cls = RegistrationBehaviour
    abci_app_cls = LiquidationStationAbciApp  # type: ignore
    behaviours: Set[Type[BaseBehaviour]] = [
        CalculatePositionHealthBehaviour,
        CollectPositionsBehaviour,
        PrepareLiquidationTransactionsBehaviour,
        RegistrationBehaviour,
        ResetAndPauseBehaviour,
        SubmitPositionLiquidationTransactionsBehaviour
    ]
