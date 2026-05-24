# auth_service.py
def authenticate(user_role: str) -> str:
    if user_role == "admin":
        return "Full Access"
    elif user_role == "editor":
        return "Write Access"
    else:
        return "Read Only"
