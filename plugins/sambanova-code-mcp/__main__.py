#!/usr/bin/env python3
# Entry point — invoked by the MCP runtime via plugin.json

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from server import mcp

if __name__ == "__main__":
    mcp.run()