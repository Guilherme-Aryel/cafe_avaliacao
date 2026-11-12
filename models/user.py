import uuid

from dataclasses import dataclass, field


@dataclass
class User:
    username: str
    password: str
    role: str = field(
        init=False,
        default="user"
    )
    id: str = field(
        init=False,
        default_factory=lambda: str(uuid.uuid4())
    )