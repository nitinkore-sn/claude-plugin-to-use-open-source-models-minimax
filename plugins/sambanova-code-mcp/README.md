# SambaNova Code MCP

MCP server that routes coding tasks to **SambaNova Cloud models** (default: MiniMax M2.7), keeping planning with Claude Opus.

- **Coding tasks** (write, debug, review, test) → SambaNova model via SambaNova Cloud
- **Planning / design / architecture** → Claude Opus/Sonnet

## Cost Comparison (MiniMax M2.7)

| Model | Input $/M tokens | Output $/M tokens |
|---|---|---|
| MiniMax M2.7 (SambaNova) | $0.60 | $2.40 |
| Claude Sonnet 4.6 | $3.00 | $15.00 |
| Claude Opus 4.7 | $5.00 | $25.00 |

MiniMax is ~20x cheaper than Opus for coding tasks.

## Tools

- `sambanova_generate_code` - Write code in any language
- `sambanova_debug_code` - Fix bugs and errors
- `sambanova_code_review` - Review and refactor code
- `sambanova_explain_code` - Explain what code does
- `sambanova_write_tests` - Write unit tests

## Setup

### Step 1 — Get a SambaNova API key

Sign up at [cloud.sambanova.ai](https://cloud.sambanova.ai) → API Keys → Create Key. Copy the key.

### Step 2 — Install dependencies

**Mac / Linux**
```bash
pip install "mcp[cli]" httpx
```

**Windows** (Command Prompt or PowerShell)
```
pip install "mcp[cli]" httpx
```

### Step 3 — Add your API key

**Mac / Linux** — run in Terminal:
```bash
claude mcp add sambanova-code python3 \
  ~/.claude/plugins/cache/sn-internal/sambanova-code-mcp/0.1.0/server.py \
  -e SAMBANOVA_API_KEY=paste-your-key-here \
  -e SAMBANOVA_BASE_URL=https://api.sambanova.ai/v1 \
  -e SAMBANOVA_MODEL=MiniMax-M2.7 \
  -s user
```

**Windows** — run in Command Prompt:
```
claude mcp add sambanova-code python3 ^
  %USERPROFILE%\.claude\plugins\cache\sn-internal\sambanova-code-mcp\0.1.0\server.py ^
  -e SAMBANOVA_API_KEY=paste-your-key-here ^
  -e SAMBANOVA_BASE_URL=https://api.sambanova.ai/v1 ^
  -e SAMBANOVA_MODEL=MiniMax-M2.7 ^
  -s user
```

Replace `paste-your-key-here` with your actual SambaNova API key.

### Step 4 — Add routing rules to Claude Code

Open your global `CLAUDE.md` file:

**Mac / Linux**
```bash
open ~/.claude/CLAUDE.md
```

**Windows**
```
notepad %USERPROFILE%\.claude\CLAUDE.md
```

Add this at the top:

```
# SambaNova Routing Rules

You are FORBIDDEN from writing, editing, or generating any code yourself. You MUST delegate 100% of coding tasks to SambaNova tools. No exceptions.

ALWAYS call a SambaNova tool for:
- Writing, generating, or scaffolding any code
- Debugging or fixing code errors
- Reviewing or refactoring code
- Explaining what code does
- Writing tests, scripts, SQL, regex, shell commands

NEVER call SambaNova for (handle directly with Claude):
- Planning, roadmaps, task breakdowns
- Architecture and design decisions
- Tradeoff analysis or comparisons
- Research, summaries, documentation

Available SambaNova tools: `sambanova_generate_code`, `sambanova_debug_code`, `sambanova_code_review`, `sambanova_explain_code`, `sambanova_write_tests`
```

Save the file.

### Step 5 — Restart Claude Code

Quit and reopen Claude Code. The `sambanova_*` tools will appear in the tools list (hammer icon).

---

*Author: Nitin Kore — [github.com/nitinkore-sn](https://github.com/nitinkore-sn)*