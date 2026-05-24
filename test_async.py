import asyncio

import pytest


# --- Application Code (Simulating an async FastAPI service layer) ---
async def fetch_user_profile(user_id: int) -> dict:
    print(f"\n[NETWORK] Fetching data for user {user_id} asynchronously...")
    # Simulate network latency
    await asyncio.sleep(0.1)
    if user_id == 843:
        return {"user_id": 843, "status": "active", "tier": "pro"}
    return {"error": "User not found"}


# --- Tests ---


# 1. We must decorate the test with @pytest.mark.asyncio
@pytest.mark.asyncio
async def test_fetch_valid_user():
    # 2. We can now use 'await' normally inside our test
    response = await fetch_user_profile(843)
    assert response["status"] == "active"
    assert response["tier"] == "pro"


@pytest.mark.asyncio
async def test_fetch_invalid_user():
    response = await fetch_user_profile(999)
    assert "error" in response
