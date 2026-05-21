# SambaNova Code MCP — Plugin Test

Test marketplace for the `sambanova-code-mcp` Claude plugin.

Routes Claude coding tasks to **MiniMax M2.7 via SambaNova Cloud** — ~8-20x cheaper than Claude Opus for code generation.

## Quick Install

**1. Install dependencies** — in Terminal:
```bash
pip install "mcp[cli]" httpx --break-system-packages
```

**2. Install plugin** — in Claude Code:
```
/plugin marketplace add https://github.com/nitinkore-sn/000-claude-plugin-test
/plugin install sambanova-code-mcp@nitinkore-sn-test
```

**3. Add API key** — in Terminal:
```bash
claude mcp add sambanova-code python3 \
  ~/.claude/plugins/cache/nitinkore-sn-test/sambanova-code-mcp/0.1.0/server.py \
  -e SAMBANOVA_API_KEY=your-key-here \
  -e SAMBANOVA_BASE_URL=https://api.sambanova.ai/v1 \
  -e SAMBANOVA_MODEL=MiniMax-M2.7 \
  -s user
```

**4. Restart Claude Code** then test:
```
write a Python function to reverse a string
```

## Requirements

- Python 3.8+
- Claude Code — [claude.ai/code](https://claude.ai/code)
- SambaNova API key — [cloud.sambanova.ai](https://cloud.sambanova.ai)

## Plugin

See [plugins/sambanova-code-mcp/README.md](plugins/sambanova-code-mcp/README.md) for full documentation.

---

*Author: Nitin Kore — [github.com/nitinkore-sn](https://github.com/nitinkore-sn)*
