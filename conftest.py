import pytest


@pytest.fixture
def mock_db_client():
    print("\n[conftest.py] Initializing mock Database connection...")
    client = {"status": "connected", "db_name": "test_db", "latency": "5ms"}

    yield client

    print("\n[conftest.py] Closing mock Database connection...")
    client.clear()


# 1. Intercepting the Setup Phase
# def pytest_runtest_setup(item):
#     # 'item' represents the test object
#     print(f"\n[HOOK: SETUP] Initializing environment for: {item.name}")


# # 2. Intercepting the Report Generation Phase
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     # Yield control back to pytest to actually run the test
#     outcome = yield
#     # Retrieve the generated report
#     report = outcome.get_result()

#     # The makereport hook fires 3 times per test (setup, call, teardown).
#     # We only care about the actual execution phase ("call").
#     if report.when == "call":
#         if report.failed:
#             print(f"\n[HOOK: MAKEREPORT] 🚨 ALERT! Test '{item.name}' FAILED.")
#         elif report.passed:
#             print(f"\n[HOOK: MAKEREPORT] ✅ Success! Test '{item.name}' PASSED.")


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="local",
        help="Environment to run tests against: local, staging, or production",
    )


# 2. Build a fixture that reads the option and generates environment config
@pytest.fixture(scope="session")
def env_config(request):
    # Retrieve the value passed to the --env flag
    selected_env = request.config.getoption("--env")

    # Define configuration baselines based on the environment
    config_matrix = {
        "local": {"base_url": "http://localhost:8000", "db_name": "dev_db"},
        "staging": {
            "base_url": "https://staging.api.ai-agent.internal",
            "db_name": "staging_db",
        },
        "production": {
            "base_url": "https://api.ai-agent.com",
            "db_name": "prod_db_readonly",
        },
    }

    # Graceful fallback error handling for unsupported environments
    if selected_env not in config_matrix:
        raise pytest.UsageError(f"Unsupported environment: --env={selected_env}")

    print(f"\n[CONFIG] Loading configuration for environment: {selected_env.upper()}")
    return config_matrix[selected_env]


def pytest_collection_modifyitems(session, config, items):
    print(f"\n[HOOK: COLLECTION] Intercepted {len(items)} tests. Reordering...")

    # 1. Separate slow tests from fast tests
    fast_tests = []
    slow_tests = []

    for item in items:
        # 2. Dynamic Skipping: Auto-skip Work-In-Progress tests
        if "wip" in item.name:
            item.add_marker(pytest.mark.skip(reason="Auto-skipped WIP test."))

        # Categorize by name
        if "slow" in item.name:
            slow_tests.append(item)
        else:
            fast_tests.append(item)

    # 3. Modify the original items list IN PLACE
    # We put all fast tests first, followed by all slow tests
    items[:] = fast_tests + slow_tests


pytest_plugins = [
    "plugins.ai_reporter"
    # As your framework grows, you can add "plugins.db_manager", etc.
]
