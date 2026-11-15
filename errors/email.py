class InvalidEmailError(ValueError):
    """Exceção base para erros de validação de e-mail."""
    def __init__(self, address: str, message: str) -> None:
        self.address = address
        super().__init__(message)


class LongEmailError(InvalidEmailError):
    """Levantada quando alguma parte do e-mail excede o tamanho máximo."""