def test_api_endpoint_resolution(env_config):
    print(f"\n  -> Target API Endpoint: {env_config['base_url']}")
    print(f"  -> Target Database: {env_config['db_name']}")

    # Assertions vary dynamically based on the input environment flag
    assert "api" in env_config["base_url"] or "localhost" in env_config["base_url"]
    assert env_config["db_name"] is not None
