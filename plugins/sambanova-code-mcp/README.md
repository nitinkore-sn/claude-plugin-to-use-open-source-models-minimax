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

## Configuration

Environment variables:
- `SAMBANOVA_API_KEY` - Your SambaNova API key (required)
- `SAMBANOVA_BASE_URL` - API base URL (default: `https://api.sambanova.ai/v1`)
- `SAMBANOVA_MODEL` - Model to use (default: `MiniMax-M2.7`)

## Setup

1. Install dependencies:
   ```bash
   pip install "mcp[cli]" httpx
   ```

2. Configure environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your SambaNova API key
   ```

3. The MCP server will be available when the plugin is installed.

## Requirements

- Python 3
- SambaNova API key from [cloud.sambanova.ai](https://cloud.sambanova.ai)

---

*Author: Nitin Kore — [github.com/nitinkore-sn](https://github.com/nitinkore-sn)*