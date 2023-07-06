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
import pytest

from camel.agents.tool_agents import WikiToolAgent
from camel.agents.tool_agents.wiki_tool_agent import LOOKUP_OP, SEARCH_OP

SEARCH_EXP = ("Saudi Arabia,[d] officially the Kingdom of Saudi Arabia (KSA)"
              ",[e] is a country in West Asia.")
LOOK_EXP = "(Result 1 / 1) Following the amalgamation"


@pytest.mark.model_backend
def test_wki_tool_agent_initialization():
    agent = WikiToolAgent("wiki_tool_agent")
    assert agent.name == "wiki_tool_agent"
    assert agent.description.startswith(f"{SEARCH_OP}[<entity>]")


@pytest.mark.model_backend
def test_wiki_tool_agent_search_step():
    agent = WikiToolAgent("wiki_tool_agent")
    result = agent.step("Saudi Arabia", SEARCH_OP)

    assert isinstance(result, str)
    assert result.startswith(SEARCH_EXP)


@pytest.mark.model_backend
def test_wiki_tool_agent_lookup_step():
    agent = WikiToolAgent("wiki_tool_agent")

    agent.step("Saudi Arabia", SEARCH_OP)
    result = agent.step("amalgamation", LOOKUP_OP)

    assert isinstance(result, str)
    assert result.startswith(LOOK_EXP)