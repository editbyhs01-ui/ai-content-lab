"""Opt-in live API smoke test; requires a real OPENAI_API_KEY."""

import os
import pytest

pytestmark = pytest.mark.integration


@pytest.mark.skipif(not os.getenv("OPENAI_API_KEY"), reason="OPENAI_API_KEY not configured")
def test_openai_api_returns_a_response():
    from konten_studio.api import check_openai_api

    result = check_openai_api()
    assert isinstance(result, str)
    assert result.strip()
