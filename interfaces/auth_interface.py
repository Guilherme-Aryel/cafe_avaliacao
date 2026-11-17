from collections.abc import Callable
from typing import Any, cast
from time import sleep

from interfaces.base import Interface
from interfaces.confirmation import YNConfirmationInterface

from models.dataclasses.user import User, UserHandler
from models.dataclasses.email import Email
from models.managers.users_manager import UserManager
from models.events_handler import EventsHandler

from errors.email import InvalidEmailError
from utils import clear_terminal
from getpass import getpass


class AuthInterface(Interface):

    def __init__(
            self,
            users_manager: UserManager,
            user_handler: UserHandler,
            events_handler: EventsHandler
        ) -> None:

        super().__init__(accepted_permissions=["admin", "user"])

        self.confirmation: YNConfirmationInterface = YNConfirmationInterface("s")

        self.user_handler: UserHandler = user_handler
        self.users_manager = users_manager
        self.events_handler: EventsHandler = events_handler
        self.dispatch_dict: dict[str, Callable[[], Any]] = {
            "cadastrar": self.register_user,
            "login": self.sign_in_user,
            "logout": self.sign_out_user,
            "sair": lambda: None
        }


    def register_user(self) -> User:
        print("Registering user...")

        user = User(
            username=self.get_username(),
            email=self.get_email(),
            password=self.get_password()
        )

        self.users_manager.register_user(user)
        print(f"Bem-vindo, {user.username}!")

        return user
    
    
    def get_email(self) -> Email:
        while True:
            address: str = input("Digite o seu email: ")
            
            try:
                return Email(address)
            except InvalidEmailError:
                print("Email inválido!\n")
    
    
    def get_username(self) -> str:
        while True:
            username: str = input("Digite um nome de usuário: ")
            
            if not username:
                print("Não deixe esse campo vazio\n")
                continue
            
            return username
    
    
    def get_password(self) -> str:
        while True:
            password: str = getpass(
                prompt="Digite uma senha: ",
                echo_char="*"
            )
            
            if not password:
                print("Não deixe esse campo vazio\n")
                continue
            
            return password


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
            
            username: str = self.get_username()
            email: Email = self.get_email()
            password: str = self.get_password()

            user: User | None = self.users_manager.get_user(username)

            if user is None:
                if register_if_not_exists:
                    confirmation: bool = self.confirmation.run(
                        "Não existe um usuário cadastrado com esses dados, deseja se cadastrar?[s/n]: "
                    )

                    if not confirmation:
                        print()
                        continue

                    user = User(username, email, password)

                    self.users_manager.register_user(user)
                    self.user_handler.update_user(user)
                    return
                
                print("Usuário não encontrado!")
                sleep(2)
                continue

            confirmation: bool = self.confirmation.run(
                "Confirma os dados inseridos?[s/n]:"
            )
            
            if not confirmation:
                continue
            
            if self.users_manager.authenticate(username, password):
                actor: User | None = self.user_handler.user
                
                self.events_handler.new_event(
                    user.id,
                    "success_to_sign_in",
                    "Alguém conseguim logar na sua conta."
                    if actor is None else
                    f"'{actor.username}' conseguiu logar na sua conta."
                )
                
                print("Usuário autenticado com sucesso!")
                self.user_handler.update_user(user)
                return
            
            current_user: User = cast(User, self.user_handler.user)          
            
            self.events_handler.new_event(
                current_user.id,
                "attempt_to_sign_in",
                f"'{current_user.username}' tentou logar na sua conta."
            )

            confirmation = self.confirmation.run(
                "Algo deu errado, deseja tentar novamente?[s/n]: "
            )

            if confirmation:
                continue
            
            if not required:
                return
            
            print("Esse login é obrigatório, aperte 's' para tentar novamente!\n")
    
    
    def sign_out_user(self) -> None:
        confirmation: bool = self.confirmation.run(
            "Deseja sair da sua conta?[s/n]: "
        )
        
        if not confirmation:
            return
        
        self.user_handler.logout()
        print("Usuário deslogado com sucesso!")
    
    
    def validate_user_permission(self, user: User) -> bool:
        return True

    def run(self) -> None:
        print("- "*20 + "Autenticação" + " -"*20)

        while True:
            print("Comandos disponíveis:")
            for command in self.dispatch_dict.keys():
                print(f"- {command}")

            entry: str = input(">>> ")

            if entry == "sair":
                return

            if entry in self.dispatch_dict:
                self.dispatch_dict[entry]()
                sleep(1)
                clear_terminal()
            else:
                print("Invalid command. Please try again.")