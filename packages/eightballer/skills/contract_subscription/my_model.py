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

"""This package contains a scaffold of a model."""

from aea.skills.base import Model

from packages.fetchai.protocols.default.dialogues import (
    DefaultDialogue,
    DefaultDialogues,
)


def get_role(*args, **kwargs) -> DefaultDialogue.Role:
    """Get the role of the agent for the dialogue."""
    return DefaultDialogue.Role.AGENT


class MyModel(Model):
    """This class scaffolds a model."""

    def setup(self) -> None:
        """Set up the model."""
        self.context.logger.info("MyModel: setup method called.")
