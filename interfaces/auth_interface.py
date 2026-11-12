from collections.abc import Callable
from typing import Any

from interfaces.base import Interface

from models.user import User
from models.users_manager import UserManager
from utils import clear_terminal


class AuthInterface(Interface):

    def __init__(
            self,
            users_manager: UserManager,
            user_to_update: User | None = None
        ) -> None:

        super().__init__(accepted_permissions=["admin", "user"])
        
        self.user_to_update: User | None = user_to_update
        self.users_manager = users_manager
        self.dispatch_dict: dict[str, Callable[[], Any]] = {
            "register_user": self.register_user,
            "sign_in_user": self.sign_in_user
        }


    def register_user(self) -> User:
        print("Registering user...")

        user = User(
            username=input("Enter username: "),
            password=input("Enter password: ")
        )

        self.users_manager.register_user(user)
        print(f"Welcome, {user.username}!")

        return user


    def sign_in_user(self, required: bool = False) -> User | None:
        print("Signing in user...")

        while True:
            username: str = input("Enter username: ")
            password: str = input("Enter password: ")
            
            if self.users_manager.authenticate(username, password):
                print("Usuário autenticado com sucesso!")
                return self.users_manager.get_user(username)

            while True:
                to_continue: str = input("Algo deu errado, deseja tentar novamente?[y/n]: ")

                match to_continue:
                    case "y": clear_terminal(); break
                    case "n":
                        if not required: return

                        print("Esse login é obrigatório, aperte 'y' para tentar novamente!")
                    case _: print("Opção inválida!")

                print()


    def run(self) -> None:
        print("-"*20, "Authentication Interface", "-"*20)

        while True:
            print("Available commands:")
            for command in self.dispatch_dict.keys():
                print(f"- {command}")

            entry: str = input(">>> ")

            if entry == "exit":
                return

            if entry in self.dispatch_dict:
                self.dispatch_dict[entry]()
            else:
                print("Invalid command. Please try again.")