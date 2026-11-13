from collections.abc import Callable
from typing import Any, cast
from time import sleep

from interfaces.base import Interface
from interfaces.confirmation import YNConfirmationInterface
from models.managers.users_manager import UserManager
from models.dataclasses.user import User, UserHandler
from errors.users import SoleAdminDeletionError
from utils import clear_terminal


class AdminInterface(Interface):
    def __init__(self, users_manager: UserManager, admin: UserHandler) -> None:
        super().__init__(accepted_permissions=["admin"])

        self.admin: UserHandler = admin
        self.users_manager = users_manager
        self.confirmation_interface: YNConfirmationInterface = YNConfirmationInterface("s")

        self.dispatch_dict: dict[str, Callable[[], Any]] = {
            "promover": self.promote_user,
            "remover": self.remove_user,
            "encontrar": self.find_user,
            "sair": lambda: None
        }


    def promote_user(self) -> None:
        username: str = input("Enter the username of the user to promote: ")
        user = self.users_manager.get_user(username)

        if user:
            user.role = "admin"
            print(f"User {username} has been promoted to admin.")
        else:
            print(f"User {username} not found.")


    def find_user(self) -> None:
        print("< digite 'cancel' para cancelar a ação >")

        while True:
            username: str = input("Digite o nome do usuário: ")

            if username == "cancel":
                return

            user: User | None = self.users_manager.get_user(username)

            if user is None:
                print("Usuário não encontrado!\n")
                continue

            print(f"Usuário encontrado: {user.username} (role: {user.role})")
            input("\nPressione Enter para continuar...")
            clear_terminal()


    def remove_user(self) -> None:
        if not self.admin.is_user_set():
            print("Sem usuário logado para realizar essa ação!")
            return

        print("< digitar 'cancel' para cancelar ação >")

        while True:
            username: str = input("Digite o nome do usuário para deletar: ")

            if username == "cancel":
                return

            user: User | None = self.users_manager.get_user(username)

            if user is None:
                print("Usuário não encontrado!\n")
                continue

            confirmation: bool = self.confirmation_interface.run(
                f"Deseja deletar '{user.username}'?[s/n]: "
            )

            if not confirmation:
                print()
                continue

            try:
                self.users_manager.remove_user(username, cast(User, self.admin.user))
            except SoleAdminDeletionError:
                print("Você é o único administrador registrado! Deletar seu registro deixará o sistema sem administradores.\n")
                continue
            
            print("Usuário removido com sucesso!")
            break
    

    def run(self) -> None:
        print("-"*20, "Admin Interface", "-"*20)

        while True:
            print("Available commands:")
            for command in self.dispatch_dict.keys():
                print(f"- {command}")

            entry: str = input(">>> ")

            if entry == "sair":
                return

            if entry in self.dispatch_dict:
                self.dispatch_dict[entry]()
            else:
                print("Opção inválida! Tente novamente.")

            sleep(1)
            clear_terminal()