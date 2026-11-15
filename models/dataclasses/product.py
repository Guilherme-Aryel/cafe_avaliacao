from dataclasses import dataclass
from typing import cast

from models.money.brl_money import BRLMoney


@dataclass
class Product:
    code: str
    name: str
    price: BRLMoney

    def __post_init__(self) -> None:
        if not self.code:
            raise ValueError("Product code cannot be empty.")
        
        if not self.name:
            raise ValueError("Product name cannot be empty.")
    
    
    def update_values(
        self,
        code: str | None = None,
        name: str | None = None,
        price: BRLMoney | None = None
    ) -> None:
        if code is not None: self.code = code
        if name is not None: self.name = name
        if price is not None: self.price = price
    

    def to_dict(self) -> dict[str, str | float]:
        return {
            "code": self.code,
            "name": self.name,
            "price": float(self.price)
        }


    @classmethod
    def from_dict(cls, data: dict[str, str | float]) -> "Product":
        return cls(
            code=cast(str, data["code"]),
            name=cast(str, data["name"]),
            price=BRLMoney.parse_from_float(cast(float, data["price"]))
        )