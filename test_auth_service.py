# test_auth_service.py
from auth_service import authenticate


def test_admin_authentication():
    result = authenticate("admin")
    assert result == "Full Access"
