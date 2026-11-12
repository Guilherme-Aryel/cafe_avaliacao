from collections.abc import Callable
from typing import Any

from interfaces.base import Interface
from models.users_manager import UserManager


class AdminInterface(Interface):
    def __init__(self, users_manager: UserManager) -> None:
        super().__init__(accepted_permissions=["admin"])
        
        self.users_manager = users_manager

        self.dispatch_dict: dict[str, Callable[[], Any]] = {
            "promote_user": self.promote_user,
            "remove_user": self.remove_user
        }


    def promote_user(self) -> None:
        username: str = input("Enter the username of the user to promote: ")
        user = self.users_manager.get_user(username)

        if user:
            user.role = "admin"
            print(f"User {username} has been promoted to admin.")
        else:
            print(f"User {username} not found.")


    def remove_user(self) -> None:
        username: str = input("Enter the username of the user to remove: ")
        success: bool = self.users_manager.remove_user(username)

        if success:
            print(f"User {username} has been removed.")
        else:
            print(f"User {username} not found.")
    

    def run(self) -> None:
        print("-"*20, "Admin Interface", "-"*20)

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