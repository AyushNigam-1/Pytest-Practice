import time

import pytest


# 'worker_id' is automatically injected by the pytest-xdist plugin
@pytest.fixture(scope="function")
def isolated_db_schema(worker_id):
    # Dynamically generate a unique schema name for the specific CPU core
    schema_name = f"schema_{worker_id}"
    print(f"\n[{worker_id}] PROVISIONING isolated schema: {schema_name}")

    # In the real world, you would run SQL here: `CREATE SCHEMA schema_gw0;`
    yield schema_name

    print(f"\n[{worker_id}] TEARING DOWN schema: {schema_name}")


def test_payment_gateway_alpha(isolated_db_schema):
    print(f"\n  -> Running Alpha test against {isolated_db_schema}")
    time.sleep(1)  # Simulate network/DB latency
    assert "gw" in isolated_db_schema


def test_payment_gateway_beta(isolated_db_schema):
    print(f"\n  -> Running Beta test against {isolated_db_schema}")
    time.sleep(1)
    assert "gw" in isolated_db_schema


def test_payment_gateway_gamma(isolated_db_schema):
    print(f"\n  -> Running Gamma test against {isolated_db_schema}")
    time.sleep(1)
    assert "gw" in isolated_db_schema
