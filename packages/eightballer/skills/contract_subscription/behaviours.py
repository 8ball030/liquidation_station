# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2023 eightballer
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

"""This package contains a scaffold of a behaviour."""
from traceback import print_exc

from aea.mail.base import Envelope
from aea.skills.behaviours import OneShotBehaviour, TickerBehaviour

from packages.eightballer.connections.websocket_client.connection import \
    CONNECTION_ID
from packages.fetchai.protocols.default.dialogues import (DefaultDialogue,
                                                          DefaultDialogues)
from packages.fetchai.protocols.default.message import DefaultMessage

subscription_msg_template = '{"jsonrpc":  "2.0",  "id":  1,  "method":  "eth_subscribe",  "params":  ["logs", {"address": "0xf25212e676d1f7f89cd72ffee66158f541246445"}]}'


class SubscriptionBehaviour(OneShotBehaviour):
    """This class scaffolds a behaviour."""

    def setup(self) -> None:
        """Implement the setup."""

    def act(self) -> None:
        """Implement the act."""
        self.context.logger.info("SubscriptionBehaviour: act called.")
        self.context.logger.info(
            "Sending subscription message: {}".format(subscription_msg_template)
        )
        self._create_subscription(bytes(subscription_msg_template, "utf-8"))
        self.context.logger.info("Act completed.")

    def teardown(self) -> None:
        """Implement the task teardown."""

    def _create_subscription(self, content: bytes):
        """Create a subscription."""
        msg, dialogue = self.context.default_dialogues.create(
            counterparty=str(CONNECTION_ID),
            performative=DefaultMessage.Performative.BYTES,
            content=content,
        )
        msg._sender = str(self.context.skill_id)
        envelope = Envelope(to=msg.to, sender=msg._sender, message=msg)
        self.context.outbox.put(envelope)


#
# class ScheduledBehaviour(TickerBehaviour):
#     """Cron Job Behaviour."""
#
#     def setup(self) -> None:
#         """Implement the setup."""
#         self.context.logger.info("CronJobBehaviour: setup method called.")
#
#     def _create_subscription(self, content: bytes):
#         """Create a subscription."""
#         msg, dialogue = self.context.default_dialogues.create(
#             counterparty=str(CONNECTION_ID),
#             performative=DefaultMessage.Performative.BYTES,
#             content=content,
#         )
#         msg._sender = str(self.context.skill_id)
#         envelope = Envelope(to=msg.to, sender=msg._sender, message=msg)
#         self.context.outbox.put(envelope)
#
#
#     def act(self) -> None:
#         """Implement the act."""
#         self.context.logger.info("CronJobBehaviour: act called.")
#         # self.context.logger.info("Sending subscription message: {}".format(subscription_msg_template))
#         # self.context.behaviours.subscriptions._create_subscription(bytes(subscription_msg_template, "utf-8"))
#         # self._create_subscription(bytes(subscription_msg_template, "utf-8"))
#         self.context.logger.info("Act completed.")
#
#
#     def teardown(self) -> None:
#         """Implement the task teardown."""
#         self.context.logger.info("CronJobBehaviour: teardown method called.")
#         self.context.logger.info("Teardown completed.")
#
#     def ___init__(self, **kwargs):
#         """Initialize."""
#         super().__init__(**kwargs)
