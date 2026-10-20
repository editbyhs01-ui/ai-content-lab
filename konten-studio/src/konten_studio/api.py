"""Minimal OpenAI API integration for a live connectivity smoke test."""

import os
from openai import OpenAI


def check_openai_api() -> str:
    """Send a tiny real request and return the response text.

    Requires OPENAI_API_KEY in the environment. This intentionally avoids
    printing credentials or request headers.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not set")

    client = OpenAI(api_key=api_key, timeout=30.0, max_retries=1)
    response = client.responses.create(
        model=os.getenv("OPENAI_TEST_MODEL", "gpt-4o-mini"),
        input="Reply with exactly: API_OK",
        max_output_tokens=16,
    )
    text = (response.output_text or "").strip()
    if not text:
        raise RuntimeError("OpenAI API returned an empty text response")
    return text
