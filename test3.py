from typing import Optional


class UserManager:
    VERSION = "1.0"

    def __init__(self):
        self.users = {}

    def add_user(self, user_id: int, name: str) -> None:
        self.users[user_id] = name

    def get_user(self, user_id: int) -> Optional[str]:
        return self.users.get(user_id)

    @staticmethod
    def validate_name(name: str) -> bool:
        return isinstance(name, str) and len(name) > 0

    @classmethod
    def get_version(cls) -> str:
        return cls.VERSION

    def _internal_helper(self, data):
        return str(data).strip()


def outer_function(x):
    def inner_function(y):
        return y * 2
    return inner_function(x)


def divide(a: float, b: float) -> float:
    try:
        return a / b
    except ZeroDivisionError:
        return 0.0


print("Module loaded successfully.")
