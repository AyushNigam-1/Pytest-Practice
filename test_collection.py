def test_slow_database_sync():
    print("  -> Executing slow DB sync...")
    assert True


def test_wip_new_feature():
    print("  -> Executing a work-in-progress feature...")
    assert False  # This would fail, but our hook will skip it!


def test_fast_math_logic():
    print("  -> Executing fast math check...")
    assert 1 + 1 == 2


def test_slow_agent_inference():
    print("  -> Executing slow AI inference...")
    assert True
