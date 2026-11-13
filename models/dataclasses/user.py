import uuid

from dataclasses import dataclass, field


@dataclass
class User:
    username: str
    password: str
    role: str = field(
        default="user"
    )
    id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )


    def to_dict(self) -> dict[str, str]:
        return {
            "username": self.username,
            "password": self.password,
            "role": self.role
        }


@dataclass
class UserHandler:
    user: User | None = None

    def update_user(self, new_user: User) -> None:
        self.user = new_user

    def is_user_set(self) -> bool:
        return self.user is not None