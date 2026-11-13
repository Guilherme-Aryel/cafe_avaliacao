from abc import ABC, abstractmethod
from collections.abc import Callable
from typing import Any

from models.dataclasses.user import User


class Interface(ABC):

    def __init__(self, accepted_permissions: list[str]) -> None:
        self.accepted_permissions: list[str] = accepted_permissions
        self.dispatch_dict: dict[str, Callable[[], Any]] = {}


    def validate_user_permission(self, user: User) -> bool:
        if user and user.role in self.accepted_permissions:
            print(f"Access granted to {self.__class__.__name__}.")
            return True
        
        print(f"Access denied to {self.__class__.__name__}.")
        return False


    def show_available_commands(self) -> None:
        print("Available commands:")
        for command in self.dispatch_dict.keys():
            print(f"- {command}")
        print("- exit")

    
    @abstractmethod
    def run(self) -> None:
        raise NotImplementedError("Subclasses must implement the run method.")