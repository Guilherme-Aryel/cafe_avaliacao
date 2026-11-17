from interfaces.base import SimpleInterface
from interfaces.confirmation import YNConfirmationInterface
from models.managers.products_manager import (
    ProductManager,
    Product,
    InexistentProductCodeError
)
from utils import clear_terminal


class UnregisterProductInterface(SimpleInterface):
    
    def __init__(self, products_manager: ProductManager) -> None:
        self.products_manager: ProductManager = products_manager
        self.confirmation: YNConfirmationInterface = YNConfirmationInterface("s")
    
    
    def run(self) -> None:
        print("Removendo produto...")

        while True:
            code: str = input("Digite o código do produto: ")

            try:
                product: Product | None = self.products_manager.get_product(code)
            except InexistentProductCodeError as e:
                print(e)
                continue
            
            if self.confirmation.run(
                f"Deseja remover '{product.name}'?[s/n]: "
            ):
                self. products_manager.unregister_product(code)
                print(f"'{product.name}' foi removido com sucesso!")
                return

            clear_terminal()
    