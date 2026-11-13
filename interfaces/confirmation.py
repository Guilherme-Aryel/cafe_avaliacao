class YNConfirmationInterface:
    def __init__(
        self,
        yes_eq: str = "y",
        no_eq: str = "n",
        invalid_op_message: str = "Opção inválida\n"
    ) -> None:
        self.yes_eq: str = yes_eq
        self.no_eq: str = no_eq
        self.invalid_op_message: str = invalid_op_message


    def run(self, text: str, invalid_op_message: str | None = None) -> bool:
        while True:
            confirmation: str = input(text)

            match confirmation:
                case self.yes_eq: return True
                case self.no_eq: return False
                case _:
                    print(
                        self.invalid_op_message
                        if invalid_op_message is None else
                        invalid_op_message
                    )