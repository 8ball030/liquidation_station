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

"""This module contains the transaction payloads of the LiquidationStationAbciApp."""

from dataclasses import dataclass

from packages.valory.skills.abstract_round_abci.base import BaseTxPayload


@dataclass(frozen=True)
class CalculatePositionHealthPayload(BaseTxPayload):
    """Represent a transaction payload for the CalculatePositionHealthRound."""

    # TODO: define your attributes


@dataclass(frozen=True)
class CollectPositionsPayload(BaseTxPayload):
    """Represent a transaction payload for the CollectPositionsRound."""

    # TODO: define your attributes


@dataclass(frozen=True)
class PrepareLiquidationTransactionsPayload(BaseTxPayload):
    """Represent a transaction payload for the PrepareLiquidationTransactionsRound."""

    # TODO: define your attributes


@dataclass(frozen=True)
class RegistrationPayload(BaseTxPayload):
    """Represent a transaction payload for the RegistrationRound."""

    # TODO: define your attributes


@dataclass(frozen=True)
class ResetAndPausePayload(BaseTxPayload):
    """Represent a transaction payload for the ResetAndPauseRound."""

    # TODO: define your attributes


@dataclass(frozen=True)
class SubmitPositionLiquidationTransactionsPayload(BaseTxPayload):
    """Represent a transaction payload for the SubmitPositionLiquidationTransactionsRound."""

    # TODO: define your attributes
