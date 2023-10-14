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

"""This module contains liquidation_listener's message definition."""

# pylint: disable=too-many-statements,too-many-locals,no-member,too-few-public-methods,too-many-branches,not-an-iterable,unidiomatic-typecheck,unsubscriptable-object
import logging
from typing import Any, Dict, Optional, Set, Tuple, cast

from aea.configurations.base import PublicId
from aea.exceptions import AEAEnforceError, enforce
from aea.protocols.base import Message

from packages.zarathustra.protocols.liquidation_listener.custom_types import (
    ErrorCode as CustomErrorCode,
)
from packages.zarathustra.protocols.liquidation_listener.custom_types import (
    Protocol as CustomProtocol,
)


_default_logger = logging.getLogger(
    "aea.packages.zarathustra.protocols.liquidation_listener.message"
)

DEFAULT_BODY_SIZE = 4


class LiquidationListenerMessage(Message):
    """A protocol for obtaining information on liquidation events."""

    protocol_id = PublicId.from_str("zarathustra/liquidation_listener:0.1.0")
    protocol_specification_id = PublicId.from_str(
        "zarathustra/liquidation_listener:0.1.0"
    )

    ErrorCode = CustomErrorCode

    Protocol = CustomProtocol

    class Performative(Message.Performative):
        """Performatives for the liquidation_listener protocol."""

        ERROR = "error"
        LIQUIDATION_EVENT = "liquidation_event"
        SUBSCRIBE_TO_LIQUIDATION_EVENTS = "subscribe_to_liquidation_events"
        UNSUBSCRIBE_FROM_LIQUIDATION_EVENTS = "unsubscribe_from_liquidation_events"
        UNSUBSCRIBED = "unsubscribed"

        def __str__(self) -> str:
            """Get the string representation."""
            return str(self.value)

    _performatives = {
        "error",
        "liquidation_event",
        "subscribe_to_liquidation_events",
        "unsubscribe_from_liquidation_events",
        "unsubscribed",
    }
    __slots__: Tuple[str, ...] = tuple()

    class _SlotsCls:
        __slots__ = (
            "block_number",
            "collateral_token_address",
            "debt_purchase_amount",
            "debt_token_address",
            "dialogue_reference",
            "error_code",
            "error_data",
            "error_msg",
            "liquidated_user",
            "liquidator_user",
            "message_id",
            "performative",
            "protocol",
            "received_amount",
            "received_token_address",
            "target",
            "trace_address",
            "transaction_hash",
        )

    def __init__(
        self,
        performative: Performative,
        dialogue_reference: Tuple[str, str] = ("", ""),
        message_id: int = 1,
        target: int = 0,
        **kwargs: Any,
    ):
        """
        Initialise an instance of LiquidationListenerMessage.

        :param message_id: the message id.
        :param dialogue_reference: the dialogue reference.
        :param target: the message target.
        :param performative: the message performative.
        :param **kwargs: extra options.
        """
        super().__init__(
            dialogue_reference=dialogue_reference,
            message_id=message_id,
            target=target,
            performative=LiquidationListenerMessage.Performative(performative),
            **kwargs,
        )

    @property
    def valid_performatives(self) -> Set[str]:
        """Get valid performatives."""
        return self._performatives

    @property
    def dialogue_reference(self) -> Tuple[str, str]:
        """Get the dialogue_reference of the message."""
        enforce(self.is_set("dialogue_reference"), "dialogue_reference is not set.")
        return cast(Tuple[str, str], self.get("dialogue_reference"))

    @property
    def message_id(self) -> int:
        """Get the message_id of the message."""
        enforce(self.is_set("message_id"), "message_id is not set.")
        return cast(int, self.get("message_id"))

    @property
    def performative(self) -> Performative:  # type: ignore # noqa: F821
        """Get the performative of the message."""
        enforce(self.is_set("performative"), "performative is not set.")
        return cast(LiquidationListenerMessage.Performative, self.get("performative"))

    @property
    def target(self) -> int:
        """Get the target of the message."""
        enforce(self.is_set("target"), "target is not set.")
        return cast(int, self.get("target"))

    @property
    def block_number(self) -> str:
        """Get the 'block_number' content from the message."""
        enforce(self.is_set("block_number"), "'block_number' content is not set.")
        return cast(str, self.get("block_number"))

    @property
    def collateral_token_address(self) -> str:
        """Get the 'collateral_token_address' content from the message."""
        enforce(
            self.is_set("collateral_token_address"),
            "'collateral_token_address' content is not set.",
        )
        return cast(str, self.get("collateral_token_address"))

    @property
    def debt_purchase_amount(self) -> int:
        """Get the 'debt_purchase_amount' content from the message."""
        enforce(
            self.is_set("debt_purchase_amount"),
            "'debt_purchase_amount' content is not set.",
        )
        return cast(int, self.get("debt_purchase_amount"))

    @property
    def debt_token_address(self) -> str:
        """Get the 'debt_token_address' content from the message."""
        enforce(
            self.is_set("debt_token_address"),
            "'debt_token_address' content is not set.",
        )
        return cast(str, self.get("debt_token_address"))

    @property
    def error_code(self) -> CustomErrorCode:
        """Get the 'error_code' content from the message."""
        enforce(self.is_set("error_code"), "'error_code' content is not set.")
        return cast(CustomErrorCode, self.get("error_code"))

    @property
    def error_data(self) -> Dict[str, str]:
        """Get the 'error_data' content from the message."""
        enforce(self.is_set("error_data"), "'error_data' content is not set.")
        return cast(Dict[str, str], self.get("error_data"))

    @property
    def error_msg(self) -> str:
        """Get the 'error_msg' content from the message."""
        enforce(self.is_set("error_msg"), "'error_msg' content is not set.")
        return cast(str, self.get("error_msg"))

    @property
    def liquidated_user(self) -> str:
        """Get the 'liquidated_user' content from the message."""
        enforce(self.is_set("liquidated_user"), "'liquidated_user' content is not set.")
        return cast(str, self.get("liquidated_user"))

    @property
    def liquidator_user(self) -> str:
        """Get the 'liquidator_user' content from the message."""
        enforce(self.is_set("liquidator_user"), "'liquidator_user' content is not set.")
        return cast(str, self.get("liquidator_user"))

    @property
    def protocol(self) -> CustomProtocol:
        """Get the 'protocol' content from the message."""
        enforce(self.is_set("protocol"), "'protocol' content is not set.")
        return cast(CustomProtocol, self.get("protocol"))

    @property
    def received_amount(self) -> int:
        """Get the 'received_amount' content from the message."""
        enforce(self.is_set("received_amount"), "'received_amount' content is not set.")
        return cast(int, self.get("received_amount"))

    @property
    def received_token_address(self) -> Optional[str]:
        """Get the 'received_token_address' content from the message."""
        return cast(Optional[str], self.get("received_token_address"))

    @property
    def trace_address(self) -> Tuple[int, ...]:
        """Get the 'trace_address' content from the message."""
        enforce(self.is_set("trace_address"), "'trace_address' content is not set.")
        return cast(Tuple[int, ...], self.get("trace_address"))

    @property
    def transaction_hash(self) -> str:
        """Get the 'transaction_hash' content from the message."""
        enforce(
            self.is_set("transaction_hash"), "'transaction_hash' content is not set."
        )
        return cast(str, self.get("transaction_hash"))

    def _is_consistent(self) -> bool:
        """Check that the message follows the liquidation_listener protocol."""
        try:
            enforce(
                isinstance(self.dialogue_reference, tuple),
                "Invalid type for 'dialogue_reference'. Expected 'tuple'. Found '{}'.".format(
                    type(self.dialogue_reference)
                ),
            )
            enforce(
                isinstance(self.dialogue_reference[0], str),
                "Invalid type for 'dialogue_reference[0]'. Expected 'str'. Found '{}'.".format(
                    type(self.dialogue_reference[0])
                ),
            )
            enforce(
                isinstance(self.dialogue_reference[1], str),
                "Invalid type for 'dialogue_reference[1]'. Expected 'str'. Found '{}'.".format(
                    type(self.dialogue_reference[1])
                ),
            )
            enforce(
                type(self.message_id) is int,
                "Invalid type for 'message_id'. Expected 'int'. Found '{}'.".format(
                    type(self.message_id)
                ),
            )
            enforce(
                type(self.target) is int,
                "Invalid type for 'target'. Expected 'int'. Found '{}'.".format(
                    type(self.target)
                ),
            )

            # Light Protocol Rule 2
            # Check correct performative
            enforce(
                isinstance(self.performative, LiquidationListenerMessage.Performative),
                "Invalid 'performative'. Expected either of '{}'. Found '{}'.".format(
                    self.valid_performatives, self.performative
                ),
            )

            # Check correct contents
            actual_nb_of_contents = len(self._body) - DEFAULT_BODY_SIZE
            expected_nb_of_contents = 0
            if (
                self.performative
                == LiquidationListenerMessage.Performative.SUBSCRIBE_TO_LIQUIDATION_EVENTS
            ):
                expected_nb_of_contents = 0
            elif (
                self.performative
                == LiquidationListenerMessage.Performative.UNSUBSCRIBE_FROM_LIQUIDATION_EVENTS
            ):
                expected_nb_of_contents = 0
            elif (
                self.performative
                == LiquidationListenerMessage.Performative.LIQUIDATION_EVENT
            ):
                expected_nb_of_contents = 10
                enforce(
                    isinstance(self.liquidated_user, str),
                    "Invalid type for content 'liquidated_user'. Expected 'str'. Found '{}'.".format(
                        type(self.liquidated_user)
                    ),
                )
                enforce(
                    isinstance(self.liquidator_user, str),
                    "Invalid type for content 'liquidator_user'. Expected 'str'. Found '{}'.".format(
                        type(self.liquidator_user)
                    ),
                )
                enforce(
                    isinstance(self.collateral_token_address, str),
                    "Invalid type for content 'collateral_token_address'. Expected 'str'. Found '{}'.".format(
                        type(self.collateral_token_address)
                    ),
                )
                enforce(
                    isinstance(self.debt_token_address, str),
                    "Invalid type for content 'debt_token_address'. Expected 'str'. Found '{}'.".format(
                        type(self.debt_token_address)
                    ),
                )
                enforce(
                    type(self.debt_purchase_amount) is int,
                    "Invalid type for content 'debt_purchase_amount'. Expected 'int'. Found '{}'.".format(
                        type(self.debt_purchase_amount)
                    ),
                )
                enforce(
                    type(self.received_amount) is int,
                    "Invalid type for content 'received_amount'. Expected 'int'. Found '{}'.".format(
                        type(self.received_amount)
                    ),
                )
                if self.is_set("received_token_address"):
                    expected_nb_of_contents += 1
                    received_token_address = cast(str, self.received_token_address)
                    enforce(
                        isinstance(received_token_address, str),
                        "Invalid type for content 'received_token_address'. Expected 'str'. Found '{}'.".format(
                            type(received_token_address)
                        ),
                    )
                enforce(
                    isinstance(self.protocol, CustomProtocol),
                    "Invalid type for content 'protocol'. Expected 'Protocol'. Found '{}'.".format(
                        type(self.protocol)
                    ),
                )
                enforce(
                    isinstance(self.transaction_hash, str),
                    "Invalid type for content 'transaction_hash'. Expected 'str'. Found '{}'.".format(
                        type(self.transaction_hash)
                    ),
                )
                enforce(
                    isinstance(self.trace_address, tuple),
                    "Invalid type for content 'trace_address'. Expected 'tuple'. Found '{}'.".format(
                        type(self.trace_address)
                    ),
                )
                enforce(
                    all(type(element) is int for element in self.trace_address),
                    "Invalid type for tuple elements in content 'trace_address'. Expected 'int'.",
                )
                enforce(
                    isinstance(self.block_number, str),
                    "Invalid type for content 'block_number'. Expected 'str'. Found '{}'.".format(
                        type(self.block_number)
                    ),
                )
            elif (
                self.performative
                == LiquidationListenerMessage.Performative.UNSUBSCRIBED
            ):
                expected_nb_of_contents = 0
            elif self.performative == LiquidationListenerMessage.Performative.ERROR:
                expected_nb_of_contents = 3
                enforce(
                    isinstance(self.error_code, CustomErrorCode),
                    "Invalid type for content 'error_code'. Expected 'ErrorCode'. Found '{}'.".format(
                        type(self.error_code)
                    ),
                )
                enforce(
                    isinstance(self.error_msg, str),
                    "Invalid type for content 'error_msg'. Expected 'str'. Found '{}'.".format(
                        type(self.error_msg)
                    ),
                )
                enforce(
                    isinstance(self.error_data, dict),
                    "Invalid type for content 'error_data'. Expected 'dict'. Found '{}'.".format(
                        type(self.error_data)
                    ),
                )
                for key_of_error_data, value_of_error_data in self.error_data.items():
                    enforce(
                        isinstance(key_of_error_data, str),
                        "Invalid type for dictionary keys in content 'error_data'. Expected 'str'. Found '{}'.".format(
                            type(key_of_error_data)
                        ),
                    )
                    enforce(
                        isinstance(value_of_error_data, str),
                        "Invalid type for dictionary values in content 'error_data'. Expected 'str'. Found '{}'.".format(
                            type(value_of_error_data)
                        ),
                    )

            # Check correct content count
            enforce(
                expected_nb_of_contents == actual_nb_of_contents,
                "Incorrect number of contents. Expected {}. Found {}".format(
                    expected_nb_of_contents, actual_nb_of_contents
                ),
            )

            # Light Protocol Rule 3
            if self.message_id == 1:
                enforce(
                    self.target == 0,
                    "Invalid 'target'. Expected 0 (because 'message_id' is 1). Found {}.".format(
                        self.target
                    ),
                )
        except (AEAEnforceError, ValueError, KeyError) as e:
            _default_logger.error(str(e))
            return False

        return True
