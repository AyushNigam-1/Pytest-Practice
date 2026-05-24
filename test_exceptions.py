import pytest


# Mock function: Validates an incoming transaction payload
def process_transaction(amount: float):
    if not isinstance(amount, (int, float)):
        raise TypeError("Transaction amount must be a number.")
    if amount <= 0:
        raise ValueError("Transaction amount must be greater than zero.")
    return f"Processed ${amount}"


def test_negative_transaction_raises_error():
    # We expect this specific block of code to raise a ValueError
    with pytest.raises(ValueError):
        process_transaction(-50.00)


def test_string_transaction_raises_type_error():
    # We can also verify the exact text of the error message using 'match'
    with pytest.raises(TypeError, match="must be a number"):
        process_transaction("one hundred dollars")


def test_zero_transaction_fails_correctly():
    with pytest.raises(ValueError, match="greater than zero"):
        process_transaction(0)
