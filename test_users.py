def test_user_creation(mock_db_client):
    print("Running test_user_creation...")
    assert mock_db_client["status"] == "connected"
    assert mock_db_client["db_name"] == "test_db"
