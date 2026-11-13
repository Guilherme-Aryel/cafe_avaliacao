class InexistentProductCodeError(Exception):
    """Raised when the product code does not exist."""

    def __init__(self, product_code: str) -> None:
        self.product_code: str = product_code
        super().__init__(f"Product with code '{self.product_code}' does not exist.")