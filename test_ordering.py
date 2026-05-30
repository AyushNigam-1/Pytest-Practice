def test_auth_service():
    print("\n  -> Checking Auth service (Pass)...")
    assert True


def test_database_sync():
    print("\n  -> Checking DB sync (Pass)...")
    assert True


def test_payment_gateway():
    print("\n  -> Checking Payment gateway (FAIL)...")
    # Simulating a broken deployment
    assert 1 == 2, "Payment API is down!"


def test_ui_dashboard():
    print("\n  -> Checking UI dashboard (Pass)...")
    assert True
