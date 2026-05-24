import pytest


# 1. Define the fixture
@pytest.fixture
def mock_user_session():
    # SETUP Phase
    print("\n[Setup] Establishing mock user session in memory...")
    session = {"user_id": 843, "role": "admin", "is_authenticated": True}

    # Yield passes the session to the test
    yield session

    # TEARDOWN Phase
    print("\n[Teardown] Destroying mock user session...")
    session.clear()


# 2. Inject the fixture into the test by passing its name
def test_admin_permissions(mock_user_session):
    print("Running test_admin_permissions...")
    assert mock_user_session["role"] == "admin"


def test_authentication_status(mock_user_session):
    print("Running test_authentication_status...")
    assert mock_user_session["is_authenticated"] is True
