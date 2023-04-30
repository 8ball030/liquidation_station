# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2023 zarathustra
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

"""Test messages module for liquidation_listener protocol."""

# pylint: disable=too-many-statements,too-many-locals,no-member,too-few-public-methods,redefined-builtin
from typing import List

from aea.test_tools.test_protocol import BaseProtocolMessagesTestCase

from packages.zarathustra.protocols.liquidation_listener.custom_types import (
    ErrorCode,
    Protocol,
)
from packages.zarathustra.protocols.liquidation_listener.message import (
    LiquidationListenerMessage,
)


class TestMessageLiquidationListener(BaseProtocolMessagesTestCase):
    """Test for the 'liquidation_listener' protocol message."""

    MESSAGE_CLASS = LiquidationListenerMessage

    def build_messages(self) -> List[LiquidationListenerMessage]:  # type: ignore[override]
        """Build the messages to be used for testing."""
        return [
            LiquidationListenerMessage(
                performative=LiquidationListenerMessage.Performative.SUBSCRIBE_TO_LIQUIDATION_EVENTS,
            ),
            LiquidationListenerMessage(
                performative=LiquidationListenerMessage.Performative.UNSUBSCRIBE_FROM_LIQUIDATION_EVENTS,
            ),
            LiquidationListenerMessage(
                performative=LiquidationListenerMessage.Performative.LIQUIDATION_EVENT,
                liquidated_user="some str",
                liquidator_user="some str",
                collateral_token_address="some str",
                debt_token_address="some str",
                debt_purchase_amount=12,
                received_amount=12,
                received_token_address="some str",
                protocol=Protocol(),  # check it please!
                transaction_hash="some str",
                trace_address=(12,),
                block_number="some str",
            ),
            LiquidationListenerMessage(
                performative=LiquidationListenerMessage.Performative.UNSUBSCRIBED,
            ),
            LiquidationListenerMessage(
                performative=LiquidationListenerMessage.Performative.ERROR,
                error_code=ErrorCode(),  # check it please!
                error_msg="some str",
                error_data={"some str": "some str"},
            ),
        ]

    def build_inconsistent(self) -> List[LiquidationListenerMessage]:  # type: ignore[override]
        """Build inconsistent messages to be used for testing."""
        return [
            LiquidationListenerMessage(
                performative=LiquidationListenerMessage.Performative.LIQUIDATION_EVENT,
                # skip content: liquidated_user
                liquidator_user="some str",
                collateral_token_address="some str",
                debt_token_address="some str",
                debt_purchase_amount=12,
                received_amount=12,
                received_token_address="some str",
                protocol=Protocol(),  # check it please!
                transaction_hash="some str",
                trace_address=(12,),
                block_number="some str",
            ),
            LiquidationListenerMessage(
                performative=LiquidationListenerMessage.Performative.ERROR,
                # skip content: error_code
                error_msg="some str",
                error_data={"some str": "some str"},
            ),
        ]
