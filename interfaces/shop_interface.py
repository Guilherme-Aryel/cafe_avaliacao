from time import sleep

from interfaces.base import Interface
from models.dataclasses.user import User
from models.managers.products_manager import ProductManager
from models.dataclasses.product import Product
from utils import clear_terminal


class ShopInterface(Interface):

    def __init__(self, products_manager: ProductManager, client: User | None) -> None:
        super().__init__(["admin", "user"])

        self.client: User | None = client
        self.product_manager: ProductManager = products_manager


    def update_client(self, client: User) -> None:
        self.client = client


    def show_title(self) -> None:
        print("="*15, "Comprar Produto", "="*15)
    

    def run(self) -> None:

        if self.client is None:
            print("Faça login em uma conta para poder fazer compras!")
            sleep(2)
            return

        while True:
            sleep(1)
            clear_terminal()
            self.show_title()
            print("('cancel' cancela a compra)")
            product_name: str = input("Digite o nome do produto: ")

            if product_name == "cancel":
                return

            product_to_buy: Product | None = self.product_manager.get_product_by_name(product_name)

            if product_to_buy is None:
                print("Produto não encontrado, tente novamente...")
                continue

            print(f"O producto escolhido custa {product_to_buy.price}")

            while True:
                confirmation: str = input("Deseja comprá-lo?[y/n]: ")

                match confirmation:
                    case "y":
                        print("Produto comprado com sucesso!")
                        # Implementar compra
                        return

                    case "n":
                        print("Encerrando compra...")
                        return

                    case _:
                        print("Opção inválida")
                        continue