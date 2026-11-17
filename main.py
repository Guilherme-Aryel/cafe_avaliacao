from time import sleep
from pathlib import Path
from typing import cast

from services.json_handler import JSONHandler
from models.managers.users_manager import UserManager
from utils import clear_terminal

from interfaces.base import Interface
from interfaces.products.products_interface import ProductInterface
from interfaces.auth_interface import AuthInterface
from interfaces.admin_interface import AdminInterface
from interfaces.shop_interface import ShopInterface
from interfaces.notifications_interface import NotificationInterface

from models.managers.products_manager import ProductManager
from models.dataclasses.user import User, UserHandler
from models.events_handler import EventsHandler


class MainInterface(Interface):
    def __init__(self) -> None:
        super().__init__(accepted_permissions=["admin", "user"])

        self.current_user: UserHandler = UserHandler()

        self.products_json_handler: JSONHandler = JSONHandler(Path("data/products.json"))
        self.users_json_handler: JSONHandler = JSONHandler(Path("data/users.json"))
        self.events_json_handler: JSONHandler = JSONHandler(Path("data/events.json"))

        self.products_manager: ProductManager = ProductManager(self.products_json_handler)
        self.users_manager: UserManager = UserManager(self.users_json_handler)
        
        self.events_handle: EventsHandler = EventsHandler(self.events_json_handler)

        self.products_interface: ProductInterface = ProductInterface(self.products_manager)
        self.authentication_interface: AuthInterface = AuthInterface(
            self.users_manager,
            self.current_user,
            self.events_handle
        )
        self.admin_interface: AdminInterface = AdminInterface(self.users_manager, self.current_user)
        self.shop_interface: ShopInterface = ShopInterface(self.products_manager, self.current_user)
        
        self.notification_interface: NotificationInterface = NotificationInterface(
            self.events_handle,
            self.current_user
        )
    
        self.interfaces: dict[str, Interface | None] = {
            "produtos": self.products_interface,
            "autenticação": self.authentication_interface,
            "admin": self.admin_interface,
            "compra": self.shop_interface,
            "notificações": self.notification_interface,
            "sair": None
        }
    

    def show_title(self) -> None:
        print("="*80)
        print(" "*20, "The Coffee - Cafeteria ")
        print("="*80)

        if self.current_user.is_user_set():
            user: User = cast(User, self.current_user.user)
            print(f"Usuário logado: {user.username} (Role: {user.role})")
        else:
            print("Nenhum usuário logado.")


    def show_available_commands(self) -> None:
        print("- "*40)
        print("Comandos disponíveis:")
        for command in self.interfaces.keys():
            print(f"- {command}")
        print("- "*40)


    def run(self) -> None:
        self.authentication_interface.sign_in_user(
            required=True,
            register_if_not_exists=True
        )
        
        sleep(1)
        while True:
            clear_terminal()
            
            self.show_title()
            self.show_available_commands()

            entry: str = input(">>> ")
    
            if entry == "sair":
                return
            
            interface: Interface | None = self.interfaces.get(entry, None)
    
            if interface and interface.validate_user_permission(cast(User, self.current_user.user)):
                clear_terminal()
                interface.run()

                sleep(1)
            else:
                print("Comando inválido! Tente novamente")
                input("Pressione Enter para continuar...")


def main() -> None:
    main_interface = MainInterface()
    main_interface.run()


if __name__ == "__main__":
    main()