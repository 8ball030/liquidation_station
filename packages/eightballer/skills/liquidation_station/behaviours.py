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

import json
from abc import ABC
from functools import cached_property
from pathlib import Path
from typing import Generator, List, Set, Type, cast

from web3 import Web3
from web3._utils.events import get_event_data

from packages.eightballer.skills.liquidation_station.models import Params
from packages.eightballer.skills.liquidation_station.rounds import (
    CalculatePositionHealthPayload,
    CalculatePositionHealthRound,
    CollectPositionsPayload,
    CollectPositionsRound,
    LiquidationStationAbciApp,
    PrepareLiquidationTransactionsPayload,
    PrepareLiquidationTransactionsRound,
    RegistrationPayload,
    RegistrationRound,
    ResetAndPausePayload,
    ResetAndPauseRound,
    SubmitPositionLiquidationTransactionsPayload,
    SubmitPositionLiquidationTransactionsRound,
    SynchronizedData,
)
from packages.valory.protocols.ledger_api.message import LedgerApiMessage
from packages.valory.skills.abstract_round_abci.base import AbstractRound
from packages.valory.skills.abstract_round_abci.behaviours import (
    AbstractRoundBehaviour,
    BaseBehaviour,
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

    def update_shared_state(
        self, accounts=None, pending_liquidations=None, done_txs=None
    ):
        """function to update the internal shared state with the current round, allowing this data to be displayed."""
        self.context.shared_state["state"]["round"] = self.behaviour_id
        if accounts is not None:
            self.context.shared_state["state"]["accounts"] = accounts
        if pending_liquidations is not None:
            self.context.shared_state["state"][
                "pending_liquidations"
            ] = pending_liquidations
        if done_txs is not None:
            self.context.shared_state["state"]["done_txs"] = done_txs

    @cached_property
    def unitroller_contract(self):  # TODO:
        INFURA_API_KEY = self.context.params.config["infura_api_key"]
        provider = f"https://polygon-mainnet.infura.io/v3/{INFURA_API_KEY}"
        unitroller_address = "0x8849f1a0cB6b5D6076aB150546EddEe193754F1C"
        path = (
            Path.cwd()
            / "vendor"
            / "zarathustra"
            / "contracts"
            / "unitroller"
            / "build"
            / "unitroller.json"
        )
        abi = json.loads(path.read_text())["abi"]
        w3 = Web3(Web3.HTTPProvider(provider))
        contract = w3.eth.contract(address=unitroller_address, abi=abi)
        return contract


class CalculatePositionHealthBehaviour(LiquidationStationBaseBehaviour):
    """CalculatePositionHealthBehaviour"""

    matching_round: Type[AbstractRound] = CalculatePositionHealthRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""

        self.context.logger.info("CalculatePositionHealthBehaviour: In the behaviour")

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = CalculatePositionHealthPayload(
                sender=sender,
            )

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

        ledger_api_response = yield from self.get_ledger_api_response(
            performative=LedgerApiMessage.Performative.GET_STATE,
            ledger_callable="get_block",
            block_identifier="latest",
        )
        correct_performative = (
            ledger_api_response.performative == LedgerApiMessage.Performative.STATE
        )
        if not correct_performative or "number" not in ledger_api_response.state.body:
            self.context.logger.error(f"Could not extract block: {ledger_api_response}")
            return

        latest_block = ledger_api_response.state.body["number"]  # 41584895

        # TODO: Now simply getting accounts that opened positions
        ## and overwrite the accounts list with the latest
        accounts = self.get_open_positions(latest_block)
        self.update_shared_state(accounts=accounts)

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = CollectPositionsPayload(
                sender=sender,
            )

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()

    def get_open_positions(self, latest_block: int) -> List[str]:

        contract = self.unitroller_contract
        event_template = contract.events.MarketEntered
        start_block = latest_block - 10_000  # TODO
        INFURA_API_KEY = self.context.params.config["infura_api_key"]
        provider = f"https://polygon-mainnet.infura.io/v3/{INFURA_API_KEY}"
        unitroller_address = "0x8849f1a0cB6b5D6076aB150546EddEe193754F1C"

        w3 = Web3(Web3.HTTPProvider(provider))
        events = w3.eth.get_logs(
            {
                "fromBlock": start_block,
                "toBlock": latest_block,
                "address": unitroller_address,
            }
        )

        def handle_event(event, event_template):
            return get_event_data(
                event_template.web3.codec, event_template._get_event_abi(), event
            )

        accounts = []
        for event in events:
            try:
                get_event_data(
                    event_template.web3.codec, event_template._get_event_abi(), event
                )
                result = handle_event(event=event, event_template=event_template)
                accounts.append(result["account"])
            except:
                # note this fails due to time contraints with streaming events
                self.context.logger.error(f"could not parse event data for {event}")

        return accounts


class PrepareLiquidationTransactionsBehaviour(LiquidationStationBaseBehaviour):
    """PrepareLiquidationTransactionsBehaviour"""

    matching_round: Type[AbstractRound] = PrepareLiquidationTransactionsRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""
        self.context.logger.info(
            "PrepareLiquidationTransactionsBehaviour: In the behaviour"
        )
        self.update_shared_state()

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = PrepareLiquidationTransactionsPayload(
                sender=sender,
            )

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
        self.update_shared_state()

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = RegistrationPayload(
                sender=sender,
            )

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
        self.update_shared_state()

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = ResetAndPausePayload(
                sender=sender,
            )

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
        self.context.logger.info(
            "SubmitPositionLiquidationTransactionsBehaviour: In the behaviour"
        )
        self.update_shared_state()

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = SubmitPositionLiquidationTransactionsPayload(
                sender=sender,
            )

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
        SubmitPositionLiquidationTransactionsBehaviour,
    ]
