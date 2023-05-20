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
import json
from abc import ABC
from typing import Generator, Set, Type, cast

from packages.valory.skills.abstract_round_abci.base import AbstractRound
from packages.valory.skills.abstract_round_abci.behaviours import (
    AbstractRoundBehaviour,
    BaseBehaviour,
)
from packages.valory.contracts.uniswap_v2_erc20.contract import UniswapV2ERC20Contract
from packages.valory.contracts.uniswap_v2_router_02.contract import (
    UniswapV2Router02Contract,
)
from packages.valory.protocols.contract_api import ContractApiMessage
from packages.valory.connections.http_client.connection import (
    PUBLIC_ID as HTTP_CLIENT_PUBLIC_ID,
)

from packages.eightballer.skills.rysk_roller.models import Params
from packages.eightballer.skills.rysk_roller.rounds import (
    SynchronizedData,
    FlowchartToFSMAbciApp,
    AnalyseDataRound,
    CallExercisedRound,
    CallExpiredRound,
    CollectDataRound,
    CollectPriceDataRound,
    MultiplexerRound,
    PutExercisedRound,
    PutExpiredRound,
    UnderAllocatedRound,
)
from packages.eightballer.skills.rysk_roller.rounds import (
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

from packages.valory.protocols.http.message import HttpMessage

DISPLAY_FORMAT = 1000000000000000000


class RyskRollerBaseBehaviour(BaseBehaviour, ABC):
    """Base behaviour for the rysk_roller skill."""

    @property
    def synchronized_data(self) -> SynchronizedData:
        """Return the synchronized data."""
        return cast(SynchronizedData, super().synchronized_data)

    @property
    def params(self) -> Params:
        """Return the params."""
        return cast(Params, super().params)


class AnalyseDataBehaviour(RyskRollerBaseBehaviour):
    """AnalyseDataBehaviour"""

    matching_round: Type[AbstractRound] = AnalyseDataRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = AnalyseDataPayload(sender=sender, )

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()


class CallExercisedBehaviour(RyskRollerBaseBehaviour):
    """CallExercisedBehaviour"""

    matching_round: Type[AbstractRound] = CallExercisedRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = CallExercisedPayload(sender=sender, )

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()


class CallExpiredBehaviour(RyskRollerBaseBehaviour):
    """CallExpiredBehaviour"""

    matching_round: Type[AbstractRound] = CallExpiredRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = CallExpiredPayload(sender=sender, )

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()


class CollectDataBehaviour(RyskRollerBaseBehaviour):
    """CollectDataBehaviour"""

    matching_round: Type[AbstractRound] = CollectDataRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""

        balances = yield from self._request_erc20_balances()
        subgraph = yield from self._request_subgraph_data()

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = CollectDataPayload(sender=sender, content={
                'balances': balances,
                'subgraph': subgraph,
            })

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()
    
    def _request_erc20_balances(self):
        """Request balance from ledger api."""
        assets = self.context.params.config['option_assets']
        balances = {}
        for name, address in assets.items():
            contract_api_msg = yield from self.get_contract_api_response(
                performative=ContractApiMessage.Performative.GET_STATE,  # type: ignore
                contract_address=address,
                contract_id=str(UniswapV2ERC20Contract.contract_id),
                contract_callable="balance_of",
                owner_address=self.context.agent_address,
            )
            balance = contract_api_msg.state.body['balance']
            self.context.logger.info(f"Requested balance for {name} at {address} is {str(balance / DISPLAY_FORMAT)}.")
            balances[name] = balance
        return balances

    def _request_subgraph_data(self):
        """Perform a http request to the subgraph api."""
        self.context.logger.info("Requesting subgraph data.")
        url = self.context.params.config['subgraph_url']
        query = self.context.params.config['subgraph_query']
        data = json.dumps({
            "query": query
        })
        response = yield from self.get_http_response(
            method="POST",
            url=url,
            content=data.encode("utf-8"),
            headers={"Content-Type": "application/json"},
        )
        response_data = json.loads(response.body)['data']
        self.context.logger.info(f"Received subgraph data: {response_data}")
        return response_data


class CollectPriceDataBehaviour(RyskRollerBaseBehaviour):
    """CollectDataBehaviour"""

    matching_round: Type[AbstractRound] = CollectPriceDataRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""

        self._request_price_data()

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = CollectPriceDataPayload(sender=sender, )

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()
    

    def _request_price_data(self):
        """Perform a contract call to the beyond pricer contract."""
        self.context.logger.info("Requesting price data.")




class MultiplexerBehaviour(RyskRollerBaseBehaviour):
    """MultiplexerBehaviour"""

    matching_round: Type[AbstractRound] = MultiplexerRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = MultiplexerPayload(sender=sender, )

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()


class PutExercisedBehaviour(RyskRollerBaseBehaviour):
    """PutExercisedBehaviour"""

    matching_round: Type[AbstractRound] = PutExercisedRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = PutExercisedPayload(sender=sender, )

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()


class PutExpiredBehaviour(RyskRollerBaseBehaviour):
    """PutExpiredBehaviour"""

    matching_round: Type[AbstractRound] = PutExpiredRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = PutExpiredPayload(sender=sender, )

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()


class UnderAllocatedBehaviour(RyskRollerBaseBehaviour):
    """UnderAllocatedBehaviour"""

    matching_round: Type[AbstractRound] = UnderAllocatedRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = UnderAllocatedPayload(sender=sender, )

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()


class FlowchartToFSMRoundBehaviour(AbstractRoundBehaviour):
    """FlowchartToFSMRoundBehaviour"""

    initial_behaviour_cls = CollectDataBehaviour
    abci_app_cls = FlowchartToFSMAbciApp  # type: ignore
    behaviours: Set[Type[BaseBehaviour]] = [
        AnalyseDataBehaviour,
        CallExercisedBehaviour,
        CallExpiredBehaviour,
        CollectDataBehaviour,
        CollectPriceDataBehaviour,
        MultiplexerBehaviour,
        PutExercisedBehaviour,
        PutExpiredBehaviour,
        UnderAllocatedBehaviour
    ]
