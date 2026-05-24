import os

import pytest


# 1. SKIP: Unconditional skip for a deprecated feature
@pytest.mark.skip(reason="Legacy v1 API endpoint is being deprecated.")
def test_legacy_v1_endpoint():
    assert False  # This would normally fail, but it gets skipped


# 2. SKIPIF: Conditional skip based on environment
# We check if 'GEMINI_API_KEY' is in the environment variables
HAS_GEMINI_KEY = os.environ.get("GEMINI_API_KEY") is not None


@pytest.mark.skipif(
    not HAS_GEMINI_KEY, reason="Skipping because GEMINI_API_KEY is missing."
)
def test_gemini_integration():
    print("Hitting the Gemini API...")
    assert True


# 3. XFAIL: Handling a known bug
@pytest.mark.xfail(
    reason="Known bug in LangChain v0.1 text splitter handling Arabic text."
)
def test_arabic_text_chunking():
    # Simulating a bug where the function crashes or returns the wrong value
    result = "broken_chunk"
    assert result == "expected_chunk"
