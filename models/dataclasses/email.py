from dataclasses import dataclass
from typing import ClassVar

from errors.email import LongEmailError


class InvalidEmailFormatError(ValueError):
    """Levantada quando o formato básico do e-mail é inválido."""

    def __init__(self, address: str, message: str = "Invalid email format.") -> None:
        self.address: str = address
        super().__init__(message)


@dataclass(frozen=True)
class Email:
    address: str

    _LENGTH: ClassVar[int] = 254
    _LOCAL_PART_LENGTH: ClassVar[int] = 64
    _DOMAIN_LENGTH: ClassVar[int] = 255
    _SUB_DOMAIN_LENGTH: ClassVar[int] = 63

    def __post_init__(self) -> None:
        normalized = self.address.strip()
        object.__setattr__(self, "address", normalized)
        self.validate_email(normalized)

    
    def validate_email(self, address: str) -> None:
        if len(address) > self._LENGTH:
            raise LongEmailError(address, "full")

        if address.count("@") != 1:
            raise InvalidEmailFormatError(
                address, "Email must contain exactly one '@' symbol."
            )

        local_part, domain = address.split("@")

        if not local_part or not domain:
            raise InvalidEmailFormatError(
                address, "Email local part and domain cannot be empty."
            )

        if len(local_part) > self._LOCAL_PART_LENGTH:
            raise LongEmailError(
                address,
                f"Email local part length must be less than or equal to {self._LOCAL_PART_LENGTH} characters."
            )

        if len(domain) > self._DOMAIN_LENGTH:
            raise LongEmailError(
                address,
                f"Email domain length must be less than or equal to {self._DOMAIN_LENGTH} characters."
            )

        if "." not in domain or domain.startswith(".") or domain.endswith("."):
            raise InvalidEmailFormatError(
                address, "Email domain must contain a valid dot separation."
            )

        subdomains: list[str] = domain.split(".")

        if any(not sub or len(sub) > self._SUB_DOMAIN_LENGTH for sub in subdomains):
            raise LongEmailError(
                address,
                f"Email subdomain length must be less than or equal to {self._SUB_DOMAIN_LENGTH} characters."
            )

    
    def __str__(self) -> str:
        return self.address