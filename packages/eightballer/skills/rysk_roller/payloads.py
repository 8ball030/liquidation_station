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

"""This module contains the transaction payloads of the FlowchartToFSMAbciApp."""

from dataclasses import dataclass

from packages.valory.skills.abstract_round_abci.base import BaseTxPayload


@dataclass(frozen=True)
class AnalyseDataPayload(BaseTxPayload):
    """Represent a transaction payload for the AnalyseDataRound."""

    # TODO: define your attributes


@dataclass(frozen=True)
class CallExercisedPayload(BaseTxPayload):
    """Represent a transaction payload for the CallExercisedRound."""

    # TODO: define your attributes


@dataclass(frozen=True)
class CallExpiredPayload(BaseTxPayload):
    """Represent a transaction payload for the CallExpiredRound."""
    # TODO: define your attributes



@dataclass(frozen=True)
class CollectDataPayload(BaseTxPayload):
    """Represent a transaction payload for the CollectDataRound."""

    content: str


@dataclass(frozen=True)
class CollectPriceDataPayload(BaseTxPayload):
    """Represent a transaction payload for the CollectDataRound."""

    content: str

@dataclass(frozen=True)
class MultiplexerPayload(BaseTxPayload):
    """Represent a transaction payload for the MultiplexerRound."""
    strategy_decision: int

    # TODO: define your attributes


@dataclass(frozen=True)
class PutExercisedPayload(BaseTxPayload):
    """Represent a transaction payload for the PutExercisedRound."""

    # TODO: define your attributes


@dataclass(frozen=True)
class PutExpiredPayload(BaseTxPayload):
    """Represent a transaction payload for the PutExpiredRound."""

    # TODO: define your attributes


@dataclass(frozen=True)
class UnderAllocatedPayload(BaseTxPayload):
    """Represent a transaction payload for the UnderAllocatedRound."""

    # TODO: define your attributes

