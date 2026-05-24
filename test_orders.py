def test_order_processing(mock_db_client):
    print("Running test_order_processing...")
    assert mock_db_client["latency"] == "5ms"
