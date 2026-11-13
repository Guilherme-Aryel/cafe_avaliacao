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