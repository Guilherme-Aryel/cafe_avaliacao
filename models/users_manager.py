from models.user import User


class UserManager:
    
    def __init__(self):
        self.users: dict[str, User] = {}


    def register_user(self, user: User) -> None:
        self.users[user.id] = user


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

    
    def remove_user(self, username: str) -> bool:
        user: User | None = self.get_user(username)
        if user:
            del self.users[user.id]
            return True
        return False