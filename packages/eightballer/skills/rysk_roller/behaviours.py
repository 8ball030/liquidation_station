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
from dataclasses import asdict
from datetime import datetime
from typing import Generator, Set, Type, cast

from packages.eightballer.skills.rysk_roller.models import (Params,
                                                            StrategyAction)
from packages.eightballer.skills.rysk_roller.rounds import (
    AnalyseDataPayload, AnalyseDataRound, CallExercisedPayload,
    CallExercisedRound, CallExpiredPayload, CallExpiredRound,
    CollectDataPayload, CollectDataRound, CollectPriceDataPayload,
    CollectPriceDataRound, FlowchartToFSMAbciApp, MultiplexerPayload,
    MultiplexerRound, PutExercisedPayload, PutExercisedRound,
    PutExpiredPayload, PutExpiredRound, SynchronizedData,
    UnderAllocatedPayload, UnderAllocatedRound)
from packages.valory.contracts.uniswap_v2_erc20.contract import \
    UniswapV2ERC20Contract
from packages.valory.protocols.contract_api import ContractApiMessage
from packages.valory.skills.abstract_round_abci.base import AbstractRound
from packages.valory.skills.abstract_round_abci.behaviours import (
    AbstractRoundBehaviour, BaseBehaviour)
from packages.zarathustra.contracts.homm_vault.contract import (
    HOMMVaultContract, OptionSeries, QuoteOptionPrice, RequestQuoteOptionPrice)

DISPLAY_FORMAT = 1000000000000000000

price_devisor = 1_000_000_000_000_000_000
exposure_devisor = 100_000_000_000_000_0000


def from_timestamp(date_string):
    """Parse a timestamp."""
    return datetime.fromtimestamp(int(date_string))


def to_human_format(row):
    """
    Format the row to align to the ccxt unified client.
    'ETH-16MAY23-1550-C'
    """

    expiration_datetime = from_timestamp(row["expiration"])
    month_code = expiration_datetime.strftime("%b").upper()
    day = expiration_datetime.strftime("%d")
    year = str(expiration_datetime.year)[2:]
    strike_price = str(int(int(row["strike"]) / price_devisor))

    return f"ETH-{day}{month_code}{year}-{strike_price}-{'P' if row['isPut'] else 'C'}"


# df = pd.DataFrame(results['series'])
#
#
# # We format the data
# df['expiration_datetime'] = df["expiration"].apply(from_timestamp)
# df['strike_price'] = df['strike'].apply(lambda x: int(int(x) / price_devisor))
# df['net_DHV_exposure'] = df['netDHVExposure'].apply(lambda x: int(int(x) / exposure_devisor))
# df["human_strike"] = df.apply(to_human_format, axis=1)


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

    def _request_erc20_balances(self, assets):
        """Request balance from ledger api."""
        balances = {}
        for name, address in assets.items():
            contract_api_msg = yield from self.get_contract_api_response(
                performative=ContractApiMessage.Performative.GET_STATE,
                # type: ignore
                contract_address=address,
                contract_id=str(UniswapV2ERC20Contract.contract_id),
                contract_callable="balance_of",
                owner_address=self.context.agent_address,
            )
            balance = contract_api_msg.state.body["balance"]
            self.context.logger.info(
                f"Requested balance for {name} at {address} is {str(balance / DISPLAY_FORMAT)}."
            )
            balances[name] = balance
        return balances


class AnalyseDataBehaviour(RyskRollerBaseBehaviour):
    """AnalyseDataBehaviour"""

    matching_round: Type[AbstractRound] = AnalyseDataRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = AnalyseDataPayload(
                sender=sender,
            )

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
            payload = CallExercisedPayload(
                sender=sender,
            )

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
            payload = CallExpiredPayload(
                sender=sender,
            )

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

        assets = self.context.params.config["option_assets"]
        subgraph = yield from self._request_subgraph_data()
        balances = yield from self._request_erc20_balances(assets)

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = CollectDataPayload(
                sender=sender,
                content=json.dumps(
                    {
                        "balances": balances,
                        "subgraph": subgraph,
                    }
                ),
            )

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()

    def _request_subgraph_data(self):
        """Perform a http request to the subgraph api."""
        self.context.logger.info("Requesting subgraph data.")
        url = self.context.params.config["subgraph_url"]
        query = self.context.params.config["subgraph_query"]
        data = json.dumps({"query": query})
        response = yield from self.get_http_response(
            method="POST",
            url=url,
            content=data.encode("utf-8"),
            headers={"Content-Type": "application/json"},
        )
        response_data = json.loads(response.body)["data"]
        self.context.logger.info(f"Received subgraph data!")
        return response_data


class CollectPriceDataBehaviour(RyskRollerBaseBehaviour):
    """CollectDataBehaviour"""

    matching_round: Type[AbstractRound] = CollectPriceDataRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""

        # positions = yield from self.get_positions()
        price_data = yield from self.get_options_prices()

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = CollectPriceDataPayload(
                sender=sender,
                content=json.dumps(
                    {
                        "price_data": price_data,
                    }
                ),
            )

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()

    def get_options_prices(
        self,
    ):
        """
        We call the beyond pricer to determine the prices for a market
        huge thanks to 0xPawel2 and Jib &&
        """
        data = self.context.state.synchronized_data.db.get("rysk_data")["subgraph"][
            "series"
        ]

        for row in data:
            if row["isBuyable"]:
                row["ask"] = yield from self._get_option_price(row, side="buy")
            if row["isSellable"]:
                row["bid"] = yield from self._get_option_price(row, side="sell")
        return data

    def get_positions(self):
        """Get the price for an option series."""

        data = self.context.state.synchronized_data.db.get("rysk_data")["subgraph"][
            "series"
        ]
        assets = {to_human_format(row): row["id"] for row in data}
        self.context.logger.info(f"Requesting positions for {len(assets)} assets.")
        balances = yield from self._request_erc20_balances(assets)
        current_positions = filter(lambda x: x["balance"] > 0, balances)
        self.context.logger.info(
            f"Received positions for {len(list(current_positions))} assets."
        )

    def _get_option_price(
        self, option_data, amount=1000000000000000000, side="buy", collateral="eth"
    ):
        """Get the price for an option series."""

        option_series = OptionSeries(
            expiration=int(option_data["expiration"]),
            strike=int(option_data["strike"]),
            is_put=bool(option_data["isPut"]),
            underlying="0x3b3a1dE07439eeb04492Fa64A889eE25A130CDd3",
            strike_asset="0x408c5755b5c7a0a28D851558eA3636CfC5b5b19d",
            collateral="0x408c5755b5c7a0a28D851558eA3636CfC5b5b19d",
        )

        request = RequestQuoteOptionPrice(
            _option_series=option_series,
            _amount=amount,
            is_sell=(side == "sell"),
            net_dhv_exposure=int(option_data["netDHVExposure"]),
        )

        # breakpoint()
        contract_api_msg = yield from self.get_contract_api_response(
            performative=ContractApiMessage.Performative.GET_STATE,
            # type: ignore
            contract_address=self.context.params.config["vault_address"],
            contract_id=str(HOMMVaultContract.contract_id),
            contract_callable="quote_option_price",
            owner_address=self.context.agent_address,
            request_quote_option_price=asdict(request),
        )
        if contract_api_msg.Performative == ContractApiMessage.Performative.ERROR:
            return {}

        quote_option_price: QuoteOptionPrice = contract_api_msg.state.body[
            "quote_option_price"
        ]
        self.context.logger.info(
            f"Received price for option series {quote_option_price}."
        )
        return quote_option_price


class MultiplexerBehaviour(RyskRollerBaseBehaviour):
    """MultiplexerBehaviour"""

    matching_round: Type[AbstractRound] = MultiplexerRound

    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""
        # we need to perform the following steps:
        # 1. check if we have any options to settle # i.e. call or puts that are expired
        # 2. if we have options to settle, we need to settle them
        # 3. if we have available funds, we need to sell options

        balances = self.context.state.synchronized_data.db.get("rysk_data")["balances"]

        # subgraph = self.context.state.synchronized_data.db.get("rysk_data")['subgraph']
        # positions = self.context.state.synchronized_data.db.get("rysk_data")['positions']

        if balances["WETH"] > self.context.params.config["min_weth"]:
            self.context.logger.info(f"Available WETH funds: {balances['WETH']}")
            decision = StrategyAction.SELL_CALL.value
        elif balances["USDC"] > self.context.params.config["min_usdc"]:
            self.context.logger.info(f"Available USDC funds: {balances['USDC']}")
            decision = StrategyAction.SELL_PUT.value
        else:
            self.context.logger.info(f"No funds available: {balances}")
            decision = StrategyAction.HOLD.value

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = MultiplexerPayload(sender=sender, strategy_decision=decision)

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()


class PutExercisedBehaviour(RyskRollerBaseBehaviour):
    """PutExercisedBehaviour"""

    matching_round: Type[AbstractRound] = PutExercisedRound

    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = PutExercisedPayload(
                sender=sender,
            )

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()

    def _build_swap_transaction(self):
        """Build the swap transaction."""
        self.context.logger.info("Building swap transaction...")


class PutExpiredBehaviour(RyskRollerBaseBehaviour):
    """PutExpiredBehaviour"""

    matching_round: Type[AbstractRound] = PutExpiredRound

    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = PutExpiredPayload(
                sender=sender,
            )

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()


class UnderAllocatedBehaviour(RyskRollerBaseBehaviour):
    """UnderAllocatedBehaviour"""

    matching_round: Type[AbstractRound] = UnderAllocatedRound

    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = UnderAllocatedPayload(
                sender=sender,
            )

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
        UnderAllocatedBehaviour,
    ]
