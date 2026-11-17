from errors.users import SoleAdminDeletionError
from models.dataclasses.user import User
from models.dataclasses.email import Email
from services.json_handler import JSONHandler


class UserManager:
    
    def __init__(self, json_handler: JSONHandler) -> None:
        self.json_handler: JSONHandler = json_handler
        self.users_data: dict[str, dict[str, str]] = self.json_handler.read_json(default={})
        self.users: dict[str, User] = self.parse_users(self.users_data)


    def count_role(self, role: str) -> int:
        return len([
            user for user in self.users.values()
            if user.role == role
        ])


    def parse_users(self, users_data: dict[str, dict[str, str]]) -> dict[str, User]:
        return {
            k: User(
                username=v["username"],
                email=Email(v["email"]),
                password=v["password"],
                role=v["role"],
                id=k
            )
            for k, v in users_data.items()
        }


    def serialize_users(self) -> dict[str, dict[str, str]]:
        return {
            k: user.to_dict()
            for k, user in self.users.items()
        }


    def register_user(self, user: User) -> None:
        self.users[user.id] = user

        self.json_handler.write_json(self.serialize_users())


    def get_user(self, username: str) -> User | None:
        for user in self.users.values():
            if user.username == username:
                return user
        
        return None
    

    def authenticate(self, username: str, password: str) -> bool:
        user: User | None = self.get_user(username)
        if user and user.password == password:
            return True
        return False


    def user_exists(self, username: str) -> bool:
        return self.get_user(username) is not None

    
    def remove_user(self, username: str, actor: User) -> bool:
        user: User | None = self.get_user(username)
        
        if not user:
            return False

        if user.role == "admin" and self.count_role("admin") == 1:
            raise SoleAdminDeletionError(actor, user)

        del self.users[user.id]
        return True