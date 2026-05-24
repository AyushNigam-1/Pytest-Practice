import pytest


@pytest.fixture
def mock_db_client():
    print("\n[conftest.py] Initializing mock Database connection...")
    client = {"status": "connected", "db_name": "test_db", "latency": "5ms"}

    yield client

    print("\n[conftest.py] Closing mock Database connection...")
    client.clear()
