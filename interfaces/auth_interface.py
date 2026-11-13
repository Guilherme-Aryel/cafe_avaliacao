from collections.abc import Callable
from typing import Any, cast
from time import sleep

from interfaces.base import Interface
from interfaces.confirmation import YNConfirmationInterface

from models.dataclasses.user import User, UserHandler
from models.managers.users_manager import UserManager
from utils import clear_terminal


class AuthInterface(Interface):

    def __init__(
            self,
            users_manager: UserManager,
            user_handler: UserHandler
        ) -> None:

        super().__init__(accepted_permissions=["admin", "user"])

        self.confirmation: YNConfirmationInterface = YNConfirmationInterface("s")

        self.user_handler: UserHandler = user_handler
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


    def sign_in_user(
            self,
            required: bool = False,
            register_if_not_exists: bool = False
        ) -> None:
        print("Logando usuário...")

        first_time: bool = True

        while True:
            if first_time:
                first_time = False
            else:
                clear_terminal()
            
            username: str = input("Digite seu nome de usuário: ")
            password: str = input("Digite sua senha: ")

            user: User | None = self.users_manager.get_user(username)

            if user is None and register_if_not_exists:
                confirmation: bool = self.confirmation.run(
                    "Não existe um usuário cadastrado com esses dados, deseja se cadastrar?[s/n]: "
                )

                if not confirmation:
                    print()
                    continue

                user = User(username, password)

                self.users_manager.register_user(user)
                self.user_handler.update_user(user)
                return
            
            if self.users_manager.authenticate(username, password):
                print("Usuário autenticado com sucesso!")
                self.user_handler.update_user(cast(User, user))
                return

            confirmation = self.confirmation.run(
                "Algo deu errado, deseja tentar novamente?[s/n]: "
            )

            if confirmation:
                continue
            
            if not required:
                return
            
            print("Esse login é obrigatório, aperte 's' para tentar novamente!\n")


    def run(self) -> None:
        print("- "*20 + "Autenticação" + " -"*20)

        while True:
            print("Comandos disponíveis:")
            for command in self.dispatch_dict.keys():
                print(f"- {command}")

            entry: str = input(">>> ")

            if entry == "exit":
                return

            if entry in self.dispatch_dict:
                self.dispatch_dict[entry]()
                sleep(1)
                clear_terminal()
            else:
                print("Invalid command. Please try again.")