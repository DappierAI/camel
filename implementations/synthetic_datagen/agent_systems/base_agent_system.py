# =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========
# Licensed under the Apache License, Version 2.0 (the “License”);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an “AS IS” BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========
from abc import ABC, abstractmethod
from dataclasses import dataclass


class BaseAgentSystem(ABC):
    @abstractmethod
    def run(self, prompt: str) -> str:
        """
        Execute the agent system with the given prompt.

        Args:
            prompt (str): The input prompt to be processed by the agent system.

        Returns:
            str: The response generated by the agent system.

        Raises:
            NotImplementedError: This method must be implemented by subclasses.
        """
        pass


@dataclass
class SyntheticDatum:
    instruction: str
    input: str
    output: str


class BaseEvalAgentSystem(ABC):
    @abstractmethod
    def run_eval(self, instruction: SyntheticDatum) -> str:
        pass
