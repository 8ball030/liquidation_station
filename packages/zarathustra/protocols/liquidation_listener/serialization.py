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

"""Serialization module for liquidation_listener protocol."""

# pylint: disable=too-many-statements,too-many-locals,no-member,too-few-public-methods,redefined-builtin
from typing import Any, Dict, cast

from aea.mail.base_pb2 import DialogueMessage
from aea.mail.base_pb2 import Message as ProtobufMessage
from aea.protocols.base import Message, Serializer

from packages.zarathustra.protocols.liquidation_listener import liquidation_listener_pb2
from packages.zarathustra.protocols.liquidation_listener.custom_types import (
    ErrorCode,
    Protocol,
)
from packages.zarathustra.protocols.liquidation_listener.message import (
    LiquidationListenerMessage,
)


class LiquidationListenerSerializer(Serializer):
    """Serialization for the 'liquidation_listener' protocol."""

    @staticmethod
    def encode(msg: Message) -> bytes:
        """
        Encode a 'LiquidationListener' message into bytes.

        :param msg: the message object.
        :return: the bytes.
        """
        msg = cast(LiquidationListenerMessage, msg)
        message_pb = ProtobufMessage()
        dialogue_message_pb = DialogueMessage()
        liquidation_listener_msg = liquidation_listener_pb2.LiquidationListenerMessage()

        dialogue_message_pb.message_id = msg.message_id
        dialogue_reference = msg.dialogue_reference
        dialogue_message_pb.dialogue_starter_reference = dialogue_reference[0]
        dialogue_message_pb.dialogue_responder_reference = dialogue_reference[1]
        dialogue_message_pb.target = msg.target

        performative_id = msg.performative
        if (
            performative_id
            == LiquidationListenerMessage.Performative.SUBSCRIBE_TO_LIQUIDATION_EVENTS
        ):
            performative = liquidation_listener_pb2.LiquidationListenerMessage.Subscribe_To_Liquidation_Events_Performative()  # type: ignore
            liquidation_listener_msg.subscribe_to_liquidation_events.CopyFrom(
                performative
            )
        elif (
            performative_id
            == LiquidationListenerMessage.Performative.UNSUBSCRIBE_FROM_LIQUIDATION_EVENTS
        ):
            performative = liquidation_listener_pb2.LiquidationListenerMessage.Unsubscribe_From_Liquidation_Events_Performative()  # type: ignore
            liquidation_listener_msg.unsubscribe_from_liquidation_events.CopyFrom(
                performative
            )
        elif (
            performative_id == LiquidationListenerMessage.Performative.LIQUIDATION_EVENT
        ):
            performative = liquidation_listener_pb2.LiquidationListenerMessage.Liquidation_Event_Performative()  # type: ignore
            liquidated_user = msg.liquidated_user
            performative.liquidated_user = liquidated_user
            liquidator_user = msg.liquidator_user
            performative.liquidator_user = liquidator_user
            collateral_token_address = msg.collateral_token_address
            performative.collateral_token_address = collateral_token_address
            debt_token_address = msg.debt_token_address
            performative.debt_token_address = debt_token_address
            debt_purchase_amount = msg.debt_purchase_amount
            performative.debt_purchase_amount = debt_purchase_amount
            received_amount = msg.received_amount
            performative.received_amount = received_amount
            if msg.is_set("received_token_address"):
                performative.received_token_address_is_set = True
                received_token_address = msg.received_token_address
                performative.received_token_address = received_token_address
            protocol = msg.protocol
            Protocol.encode(performative.protocol, protocol)
            transaction_hash = msg.transaction_hash
            performative.transaction_hash = transaction_hash
            trace_address = msg.trace_address
            performative.trace_address.extend(trace_address)
            block_number = msg.block_number
            performative.block_number = block_number
            liquidation_listener_msg.liquidation_event.CopyFrom(performative)
        elif performative_id == LiquidationListenerMessage.Performative.UNSUBSCRIBED:
            performative = liquidation_listener_pb2.LiquidationListenerMessage.Unsubscribed_Performative()  # type: ignore
            liquidation_listener_msg.unsubscribed.CopyFrom(performative)
        elif performative_id == LiquidationListenerMessage.Performative.ERROR:
            performative = liquidation_listener_pb2.LiquidationListenerMessage.Error_Performative()  # type: ignore
            error_code = msg.error_code
            ErrorCode.encode(performative.error_code, error_code)
            error_msg = msg.error_msg
            performative.error_msg = error_msg
            error_data = msg.error_data
            performative.error_data.update(error_data)
            liquidation_listener_msg.error.CopyFrom(performative)
        else:
            raise ValueError("Performative not valid: {}".format(performative_id))

        dialogue_message_pb.content = liquidation_listener_msg.SerializeToString()

        message_pb.dialogue_message.CopyFrom(dialogue_message_pb)
        message_bytes = message_pb.SerializeToString()
        return message_bytes

    @staticmethod
    def decode(obj: bytes) -> Message:
        """
        Decode bytes into a 'LiquidationListener' message.

        :param obj: the bytes object.
        :return: the 'LiquidationListener' message.
        """
        message_pb = ProtobufMessage()
        liquidation_listener_pb = liquidation_listener_pb2.LiquidationListenerMessage()
        message_pb.ParseFromString(obj)
        message_id = message_pb.dialogue_message.message_id
        dialogue_reference = (
            message_pb.dialogue_message.dialogue_starter_reference,
            message_pb.dialogue_message.dialogue_responder_reference,
        )
        target = message_pb.dialogue_message.target

        liquidation_listener_pb.ParseFromString(message_pb.dialogue_message.content)
        performative = liquidation_listener_pb.WhichOneof("performative")
        performative_id = LiquidationListenerMessage.Performative(str(performative))
        performative_content = dict()  # type: Dict[str, Any]
        if (
            performative_id
            == LiquidationListenerMessage.Performative.SUBSCRIBE_TO_LIQUIDATION_EVENTS
        ):
            pass
        elif (
            performative_id
            == LiquidationListenerMessage.Performative.UNSUBSCRIBE_FROM_LIQUIDATION_EVENTS
        ):
            pass
        elif (
            performative_id == LiquidationListenerMessage.Performative.LIQUIDATION_EVENT
        ):
            liquidated_user = liquidation_listener_pb.liquidation_event.liquidated_user
            performative_content["liquidated_user"] = liquidated_user
            liquidator_user = liquidation_listener_pb.liquidation_event.liquidator_user
            performative_content["liquidator_user"] = liquidator_user
            collateral_token_address = (
                liquidation_listener_pb.liquidation_event.collateral_token_address
            )
            performative_content["collateral_token_address"] = collateral_token_address
            debt_token_address = (
                liquidation_listener_pb.liquidation_event.debt_token_address
            )
            performative_content["debt_token_address"] = debt_token_address
            debt_purchase_amount = (
                liquidation_listener_pb.liquidation_event.debt_purchase_amount
            )
            performative_content["debt_purchase_amount"] = debt_purchase_amount
            received_amount = liquidation_listener_pb.liquidation_event.received_amount
            performative_content["received_amount"] = received_amount
            if liquidation_listener_pb.liquidation_event.received_token_address_is_set:
                received_token_address = (
                    liquidation_listener_pb.liquidation_event.received_token_address
                )
                performative_content["received_token_address"] = received_token_address
            pb2_protocol = liquidation_listener_pb.liquidation_event.protocol
            protocol = Protocol.decode(pb2_protocol)
            performative_content["protocol"] = protocol
            transaction_hash = (
                liquidation_listener_pb.liquidation_event.transaction_hash
            )
            performative_content["transaction_hash"] = transaction_hash
            trace_address = liquidation_listener_pb.liquidation_event.trace_address
            trace_address_tuple = tuple(trace_address)
            performative_content["trace_address"] = trace_address_tuple
            block_number = liquidation_listener_pb.liquidation_event.block_number
            performative_content["block_number"] = block_number
        elif performative_id == LiquidationListenerMessage.Performative.UNSUBSCRIBED:
            pass
        elif performative_id == LiquidationListenerMessage.Performative.ERROR:
            pb2_error_code = liquidation_listener_pb.error.error_code
            error_code = ErrorCode.decode(pb2_error_code)
            performative_content["error_code"] = error_code
            error_msg = liquidation_listener_pb.error.error_msg
            performative_content["error_msg"] = error_msg
            error_data = liquidation_listener_pb.error.error_data
            error_data_dict = dict(error_data)
            performative_content["error_data"] = error_data_dict
        else:
            raise ValueError("Performative not valid: {}.".format(performative_id))

        return LiquidationListenerMessage(
            message_id=message_id,
            dialogue_reference=dialogue_reference,
            target=target,
            performative=performative,
            **performative_content
        )
