from abc import ABC, abstractmethod
from collections.abc import Callable
from typing import Any


class Interface(ABC):

    def __init__(self, accepted_permissions: list[str]) -> None:
        self.accepted_permissions: list[str] = accepted_permissions
        self.dispatch_dict: dict[str, Callable[[], Any]] = {}


    def show_available_commands(self) -> None:
        print("Available commands:")
        for command in self.dispatch_dict.keys():
            print(f"- {command}")
        print("- exit")

    
    @abstractmethod
    def run(self) -> None:
        raise NotImplementedError("Subclasses must implement the run method.")