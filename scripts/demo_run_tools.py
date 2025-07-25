"""
This script demonstrates how to use Serena's tools locally, useful
for testing or development. Here the tools will be operation the serena repo itself.
"""

import json
from pprint import pprint

from serena.agent import SerenaAgent
from serena.config.serena_config import SerenaConfig
from serena.constants import REPO_ROOT
from serena.tools import FindFileTool, FindReferencingSymbolsTool, SearchForPatternTool

if __name__ == "__main__":
    agent = SerenaAgent(project=REPO_ROOT, serena_config=SerenaConfig(gui_log_window_enabled=False, web_dashboard=False))

    # apply a tool
    find_refs_tool = agent.get_tool(FindReferencingSymbolsTool)
    find_file_tool = agent.get_tool(FindFileTool)
    search_pattern_tool = agent.get_tool(SearchForPatternTool)

    result = agent.execute_task(
        lambda: search_pattern_tool.apply(
            r"def request_full_.*?\).*?\)",
            restrict_search_to_code_files=False,
            relative_path="src/solidlsp",
            paths_include_glob="**/ls.py",
        )
    )
    pprint(json.loads(result))
