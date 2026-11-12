from typing import Any

from models.money.base import Money


class BRLMoney(Money):
    def __init__(self, reais: int, centavos: int) -> None:
        super().__init__("BRL")

        self.validate(reais, centavos)

        self.reais: int = reais
        self.centavos: int = centavos
        self.cents: int = reais * 100 + centavos


    def __str__(self) -> str:
        return f"R${self.reais},{self.centavos:02d}"


    def __repr__(self) -> str:
        return f"BRLMoney(reais={self.reais}, centavos={self.centavos})"


    def __float__(self) -> float:
        return self.reais + self.centavos / 100.0

    
    def __int__(self) -> int:
        return self.reais


    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, BRLMoney):
            return NotImplemented
        return self.cents == other.cents


    def __lt__(self, other: Any) -> bool:
        if not isinstance(other, BRLMoney):
            return NotImplemented
        return self.cents < other.cents


    def __le__(self, other: Any) -> bool:
        if not isinstance(other, BRLMoney):
            return NotImplemented
        return self.cents <= other.cents


    def __gt__(self, other: Any) -> bool:
        if not isinstance(other, BRLMoney):
            return NotImplemented
        return self.cents > other.cents


    def __ge__(self, other: Any) -> bool:
        if not isinstance(other, BRLMoney):
            return NotImplemented
        return self.cents >= other.cents


    def __add__(self, other: Any) -> "BRLMoney":
        if not isinstance(other, BRLMoney):
            return NotImplemented
        total_cents: int = self.cents + other.cents
        return BRLMoney(total_cents // 100, total_cents % 100)


    def __sub__(self, other: Any) -> "BRLMoney":
        if not isinstance(other, BRLMoney):
            return NotImplemented
        total_cents: int = self.cents - other.cents
        if total_cents < 0:
            raise ValueError("Resulting amount cannot be negative.")
        return BRLMoney(total_cents // 100, total_cents % 100)


    def __mul__(self, other: Any) -> "BRLMoney":
        if not isinstance(other, (int, float)):
            return NotImplemented
        total_cents: int = int(round(self.cents * other))
        return BRLMoney(total_cents // 100, total_cents % 100)


    def __truediv__(self, other: Any) -> "BRLMoney":
        if not isinstance(other, (int, float)):
            return NotImplemented
        if other == 0:
            raise ValueError("Cannot divide by zero.")
        total_cents: int = int(round(self.cents / other))
        return BRLMoney(total_cents // 100, total_cents % 100)


    def __mod__(self, other: Any) -> "BRLMoney":
        if not isinstance(other, BRLMoney):
            return NotImplemented
        total_cents: int = self.cents % other.cents
        return BRLMoney(total_cents // 100, total_cents % 100)


    def __neg__(self) -> "BRLMoney":
        raise ValueError("BRLMoney cannot be negative.")


    def __abs__(self) -> "BRLMoney":
        return self


    def __hash__(self) -> int:
        return hash((self.reais, self.centavos))


    def __copy__(self) -> "BRLMoney":
        return BRLMoney(self.reais, self.centavos)


    def validate(self, reais: int, centavos: int) -> None:
        if reais < 0 or centavos < 0:
            raise ValueError("Reais and centavos must be non-negative.")
        if centavos >= 100:
            raise ValueError("Centavos must be less than 100.")
    
    # =====================================================================================
    #                  Parsing Methods
    # =====================================================================================

    @classmethod
    def parse_from_string(cls, value: str) -> "BRLMoney":
        if not value.startswith("R$"):
            raise ValueError("Value must start with 'R$'.")

        value = value[2:].strip()
        if "," in value:
            reais_str, centavos_str = value.split(",")
            reais: int = int(reais_str)
            centavos: int = int(centavos_str)
        else:
            reais: int = int(value)
            centavos: int = 0

        return cls(reais, centavos)


    @classmethod
    def parse_from_float(cls, value: float) -> "BRLMoney":
        if value < 0:
            raise ValueError("Value must be non-negative.")

        reais: int = int(value)
        centavos: int = int(round((value - reais) * 100))
        return cls(reais, centavos)


    @classmethod
    def parse_from_int(cls, value: int) -> "BRLMoney":
        if value < 0:
            raise ValueError("Value must be non-negative.")

        return cls(value, 0)


    @classmethod
    def parse(cls, value: Any) -> "BRLMoney":
        if isinstance(value, str):
            return cls.parse_from_string(value)

        elif isinstance(value, float):
            return cls.parse_from_float(value)
        elif isinstance(value, int):
            return cls.parse_from_int(value)

        raise ValueError("Value must be a float, int, or str.")
