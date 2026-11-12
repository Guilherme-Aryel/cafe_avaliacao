from abc import ABC
from dataclasses import dataclass


@dataclass
class Money(ABC):
    currency: str