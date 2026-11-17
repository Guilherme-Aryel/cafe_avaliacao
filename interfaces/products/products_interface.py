from collections.abc import Callable
from time import sleep

from errors.product import InexistentProductCodeError
from interfaces.base import Interface
from models.money.brl_money import BRLMoney
from models.dataclasses.product import Product
from models.managers.products_manager import ProductManager
from interfaces.confirmation import YNConfirmationInterface
from utils import clear_terminal

from interfaces.products.show_products_interface import ShowProductsInterface
from interfaces.products.change_product_interface import ChangeProductInterface
from interfaces.products.product_getters import ProductGetters


class ProductInterface(Interface):

    def __init__(self, products_manager: ProductManager) -> None:
        super().__init__(accepted_permissions=["admin"])
        
        self.confirmation: YNConfirmationInterface = YNConfirmationInterface("s")
        
        self.products_manager: ProductManager = products_manager
        self.product_getters: ProductGetters = ProductGetters(self.products_manager)
        
        self.show_products_interface: ShowProductsInterface = ShowProductsInterface(
            self.products_manager
        )
        
        self.change_product_interface: ChangeProductInterface = ChangeProductInterface(
            self.products_manager, self.product_getters
        )
        
        self.command_dispatch: dict[str, Callable[[], None]] = {
            "registrar": self.register_product,
            "editar": self.change_product,
            "remover": self.unregister_product,
            "estocar": self.stock_product,
            "mostrar": self.show_products,
            "sair": lambda: None
        }
    
    # =============================================================
    #                        EXHIBITION
    # =============================================================
    
    def show_title(self) -> None:
        print("="*40)
        print(" "*10, "Produtos")
        print("="*40)


    def show_options(self) -> None:
        for command in self.command_dispatch.keys():
            print(f"- {command}")
        print("- "*20)
    
    # =============================================================
    #                        OPTIONS
    # =============================================================
    
    def change_product(self) -> None:
        self.change_product_interface.run()
    

    def register_product(self) -> None:
        print("Registrando novo produto...")
        
        while True:
            code: str = self.product_getters.get_product_code()
            name: str = self.product_getters.get_product_name()
            price: float = self.product_getters.get_product_price()
            
            if self.confirmation.run(
                "Deseja registrar esse produto?[s/n]: "
            ):
                break
        
        product: Product = Product(
            code,
            name,
            price=BRLMoney.parse_from_float(price)
        )

        self.products_manager.register_product(product)
        print(f"'{product.name}' foi registrado com sucesso como produto!")


    def unregister_product(self) -> None:
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
    

    def show_products(self) -> None:
        self.show_products_interface.run()
    
    
    def get_quantity(self) -> int:
        while True:
            try:
                return int(input(
                    f"Digite a quantidade de produtos que deseja estocar: ")
                )
            except ValueError:
                print("Digite um valor númerico!\n")
                continue


    def stock_product(self) -> None:
        print("Estocando produto...")
        
        while True:
            product: Product = self.product_getters.get_product_by_code()
            quantity: int = self.get_quantity()
            
            while True:
                print("Deseja incrementar ou definir do zero o estoque com o valor fornecido?")
                print("1 - incrementar\n2 - definir")
                choice: str = input(">>> ")

                match choice:
                    case "1":
                        self.products_manager.increase_stock(product.code, quantity)
                        break

                    case "2":
                        self.products_manager.set_stock(product.code, quantity)
                        break

                    case _:
                        print("Opção inválida\n")

            print(f"Stocked {quantity} units of {product.name}.")
                               

    def run(self) -> None:
        while True:
            self.show_title()
            self.show_options()
            entry: str = input(">>> ")

            if entry == "exit":
                return

            if entry in self.command_dispatch:
                clear_terminal()
                self.command_dispatch[entry]()
                sleep(1)
                clear_terminal()
            else:
                print("Invalid command. Please try again.")