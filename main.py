from time import sleep
from pathlib import Path
from typing import cast

from models.json_handler import JSONHandler
from models.users_manager import UserManager
from utils import clear_terminal

from interfaces.base import Interface
from interfaces.products_interface import ProductInterface
from interfaces.auth_interface import AuthInterface
from interfaces.admin_interface import AdminInterface
from interfaces.shop_interface import ShopInterface

from models.products_manager import ProductManager
from models.user import User


def validate_user_permission(
    current_user: User | None,
    interface: Interface
) -> bool:
    if current_user is not None and current_user.role in interface.accepted_permissions:
        print(f"Access granted to {interface.__class__.__name__}.")
        return True
    
    print(f"Access denied to {interface.__class__.__name__}.")
    return False


class MainInterface(Interface):
    def __init__(self) -> None:
        super().__init__(accepted_permissions=["admin", "user"])

        self.current_user: User | None = None

        self.products_json_handler: JSONHandler = JSONHandler(Path("data/products.json"))
        self.users_json_handler: JSONHandler = JSONHandler(Path("data/users.json"))

        self.products_manager: ProductManager = ProductManager(self.products_json_handler)
        self.users_manager: UserManager = UserManager(self.users_json_handler)

        self.products_interface: ProductInterface = ProductInterface(self.products_manager)
        self.authentication_interface: AuthInterface = AuthInterface(self.users_manager, user_to_update=self.current_user)
        self.admin_interface: Interface = AdminInterface(self.users_manager)
        self.shop_interface: ShopInterface = ShopInterface(self.products_manager, self.current_user)
    
        self.interfaces: dict[str, Interface | None] = {
            "products": self.products_interface,
            "authentication": self.authentication_interface,
            "admin": self.admin_interface,
            "shop": self.shop_interface,
            "exit": None
        }
    

    def show_title(self) -> None:
        print("-"*20, "The Coffee", "-"*20)
        if self.current_user:
            print(f"Current user: {self.current_user.username} (Role: {self.current_user.role})")
        else:
            print("No user is currently logged in.")


    def show_available_commands(self) -> None:
        print("Available commands:")
        for command in self.interfaces.keys():
            print(f"- {command}")


    def run(self) -> None:
        self.current_user = self.authentication_interface.sign_in_user(required=True)

        self.shop_interface.update_client(cast(User, self.current_user))
        
        sleep(1)
        while True:
            clear_terminal()

            self.show_title()
            self.show_available_commands()

            entry: str = input(">>> ")
    
            if entry == "exit":
                return
            
            interface: Interface | None = self.interfaces.get(entry, None)
    
            if interface and validate_user_permission(self.current_user, interface):
                clear_terminal()
                interface.run()

                sleep(1)
            else:
                print("Invalid command. Please try again.")
                input("Press Enter to continue...")


def main() -> None:
    main_interface = MainInterface()
    main_interface.run()


if __name__ == "__main__":
    main()