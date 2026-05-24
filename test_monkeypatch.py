import os

import pytest


# --- Application Code (Usually in a separate file like config.py or agent.py) ---
def get_database_url():
    # Falls back to an in-memory SQLite DB if the environment variable is missing
    return os.environ.get("POSTGRES_URL", "sqlite:///:memory:")


class DocumentAnalyzer:
    def fetch_llm_summary(self, text: str) -> str:
        # In real life, this makes a slow HTTP request to the Gemini API
        print("\n[NETWORK CALL] Reaching out to Gemini API...")
        return "Real API Response: This document is about Python testing."


# --- Tests ---
def test_database_url_picks_up_env_var(monkeypatch):
    # 1. Mocking an OS environment variable
    fake_db_url = "postgresql://user:pass@localhost:5432/test_db"
    monkeypatch.setenv("POSTGRES_URL", fake_db_url)

    # The application code now magically sees our fake environment variable
    assert get_database_url() == fake_db_url


def test_document_analyzer_bypasses_network(monkeypatch):
    # 2. Mocking a function (method) to bypass network calls
    analyzer = DocumentAnalyzer()

    # FIX: We add 'self' as the first parameter to accept the class instance
    def fake_fetch(self, text: str) -> str:
        print("\n[MOCKED] Returning instant fake response!")
        return "Mocked API Response: Fast and free!"

    monkeypatch.setattr(DocumentAnalyzer, "fetch_llm_summary", fake_fetch)

    result = analyzer.fetch_llm_summary("Some text")

    assert result == "Mocked API Response: Fast and free!"
