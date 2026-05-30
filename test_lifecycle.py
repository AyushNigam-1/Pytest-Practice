def test_database_connection():
    print("  -> Executing test_database_connection body...")
    assert True


def test_agent_timeout():
    print("  -> Executing test_agent_timeout body...")
    # Deliberately failing this test to trigger our custom hook logic
    assert 1 == 2
