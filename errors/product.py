class InexistentProductCodeError(Exception):
    """Raised when the product code does not exist."""

    def __init__(self, product_code: str) -> None:
        super().__init__(f"Product with code '{product_code}' does not exist.")