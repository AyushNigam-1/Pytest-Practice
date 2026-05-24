import pytest


# 1. SESSION SCOPE: Runs only once for the entire test run
@pytest.fixture(scope="session")
def postgres_pool():
    print("\n[SETUP - SESSION] Opening PostgreSQL connection pool...")
    # Simulate connecting to the DB
    pool = {"status": "connected", "max_connections": 10}

    yield pool

    print("\n[TEARDOWN - SESSION] Closing PostgreSQL connection pool...")
    pool.clear()


# 2. FUNCTION SCOPE (default): Runs for every single test
@pytest.fixture
def db_transaction(postgres_pool):
    # Notice that a fixture can request another fixture!
    print("\n  [SETUP - FUNCTION] Starting DB transaction...")
    transaction_id = "txn_843"

    yield transaction_id

    print("\n  [TEARDOWN - FUNCTION] Rolling back DB transaction...")


# --- Tests ---


def test_document_embedding_insert(db_transaction):
    print(f"    Running test_document_embedding_insert with {db_transaction}...")
    assert True


def test_user_retrieval_query(db_transaction):
    print(f"    Running test_user_retrieval_query with {db_transaction}...")
    assert True
