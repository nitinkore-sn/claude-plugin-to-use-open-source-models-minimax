#!/usr/bin/env python3
# Author: Nitin Kore
# SambaNova MCP server — routes coding tasks to SambaNova Cloud models (default: MiniMax M2.7)

import sys
import os

try:
    import httpx
    from mcp.server.fastmcp import FastMCP
except ImportError:
    print("Missing dependencies. Run: pip install \"mcp[cli]\" httpx", file=sys.stderr)
    sys.exit(1)

mcp = FastMCP("sambanova-code")

BASE_URL = os.environ.get("SAMBANOVA_BASE_URL", "https://api.sambanova.ai/v1")
MODEL = os.environ.get("SAMBANOVA_MODEL", "MiniMax-M2.7")

MAX_DESC_LEN = 2000
MAX_CODE_LEN = 8000


@mcp.tool()
def sambanova_generate_code(description: str, language: str = "Python", context: str = "") -> str:
    """
    Generate code using SambaNova Cloud models. Use for writing, scaffolding, or creating
    new code in any language. Claude handles reading/writing files — this tool returns
    generated code as text. Pass relevant file content via the context parameter.
    """
    if len(description) > MAX_DESC_LEN:
        raise ValueError(f"description exceeds {MAX_DESC_LEN} characters")
    if len(context) > MAX_CODE_LEN:
        raise ValueError(f"context exceeds {MAX_CODE_LEN} characters")
    ctx = f"\n\nExisting context:\n{context}" if context else ""
    prompt = f"Write {language} code for: {description}{ctx}\n\nReturn only the code with brief inline comments where non-obvious."
    return _call(prompt, system=f"You are an expert {language} developer. Return clean, production-ready code.")


@mcp.tool()
def sambanova_debug_code(code: str, error: str = "", language: str = "") -> str:
    """
    Debug and fix code using SambaNova Cloud models. Use when the user has a bug or error.
    Returns the fixed code as text — Claude handles applying it to files.
    """
    if len(code) > MAX_CODE_LEN:
        raise ValueError(f"code exceeds {MAX_CODE_LEN} characters")
    err_hint = f"\n\nError message:\n{error}" if error else ""
    prompt = f"Find and fix the bug in this {language} code:{err_hint}\n\n```{language}\n{code}\n```\n\nReturn the fixed code and a one-line explanation of the fix."
    return _call(prompt, system="You are an expert debugger. Be precise and minimal — change only what is broken.")


@mcp.tool()
def sambanova_code_review(code: str, language: str = "", instructions: str = "") -> str:
    """
    Review and refactor code using SambaNova Cloud models. Use when the user wants
    code quality feedback or improvements. Returns review comments and suggestions as text.
    """
    if len(code) > MAX_CODE_LEN:
        raise ValueError(f"code exceeds {MAX_CODE_LEN} characters")
    extra = f"\n\nFocus on: {instructions}" if instructions else ""
    prompt = f"Review this {language} code for bugs, issues, and improvements:\n\n```{language}\n{code}\n```{extra}"
    return _call(prompt, system="You are an expert code reviewer. Be concise and specific. Prioritize correctness, then clarity.")


@mcp.tool()
def sambanova_explain_code(code: str, language: str = "") -> str:
    """
    Explain what code does using SambaNova Cloud models. Use when the user wants
    to understand a piece of code. Returns a plain-language explanation as text.
    """
    if len(code) > MAX_CODE_LEN:
        raise ValueError(f"code exceeds {MAX_CODE_LEN} characters")
    prompt = f"Explain what this {language} code does, step by step:\n\n```{language}\n{code}\n```"
    return _call(prompt, system="Explain clearly and concisely. Focus on the 'why', not just the 'what'.")


@mcp.tool()
def sambanova_write_tests(code: str, language: str = "Python", framework: str = "") -> str:
    """
    Write unit tests for code using SambaNova Cloud models. Use when the user wants
    test coverage for existing code. Returns test code as text — Claude handles
    creating the test file.
    """
    if len(code) > MAX_CODE_LEN:
        raise ValueError(f"code exceeds {MAX_CODE_LEN} characters")
    fw = f" using {framework}" if framework else ""
    prompt = f"Write thorough unit tests{fw} for this {language} code:\n\n```{language}\n{code}\n```"
    return _call(prompt, system=f"You are an expert in {language} testing. Cover happy path, edge cases, and error cases.")


def _call(prompt: str, system: str = "") -> str:
    api_key = os.environ.get("SAMBANOVA_API_KEY", "")
    if not api_key:
        raise RuntimeError("SAMBANOVA_API_KEY is not set. Run: claude mcp add sambanova-code ... -e SAMBANOVA_API_KEY=your-key")

    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})

    try:
        with httpx.Client(timeout=120) as client:
            resp = client.post(
                f"{BASE_URL}/chat/completions",
                headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
                json={"model": MODEL, "messages": messages},
            )
            resp.raise_for_status()
            return resp.json()["choices"][0]["message"]["content"]
    except httpx.HTTPStatusError as e:
        raise RuntimeError(f"SambaNova API error: {e.response.status_code}") from None
    except httpx.RequestError:
        raise RuntimeError("Could not reach SambaNova API. Check your network connection.") from None


if __name__ == "__main__":
    mcp.run()
