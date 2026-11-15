from collections.abc import Callable
from time import sleep

from errors.product import InexistentProductCodeError
from interfaces.base import Interface
from models.money.brl_money import BRLMoney
from models.dataclasses.product import Product
from models.managers.products_manager import ProductManager
from utils import clear_terminal


class ProductInterface(Interface):

    def __init__(self, products_manager: ProductManager) -> None:
        super().__init__(accepted_permissions=["admin"])

        self.products_manager: ProductManager = products_manager
        self.command_dispatch: dict[str, Callable[[], None]] = {
            "registrar": self.register_product,
            "editar": self.change_product,
            "remover": self.unregister_product,
            "estocar": self.stock_product,
            "mostrar": self.show_products,
            "sair": lambda: None
        }


    def show_options(self) -> None:
        print("Comandos disponíveis:")
        for command in self.command_dispatch.keys():
            print(f"- {command}")


    def get_product_code(self) -> str:
        while True:
            code: str = input("Digite o código do produto: ")

            if not code:
                print("Valor inválido! Digite algum valor para ser o código do produto\n")
                continue

            if code in self.products_manager.product_codes:
                print("Código de produto já cadastrado!")
                continue

            return code


    def get_product_name(self) -> str:
        while True:
            name: str = input("Digite o nome do produto: ")

            if not name:
                print("Valor inválido! Digite algum valor para ser o código do produto\n")
                continue

            return name


    def get_product_price(self) -> float:
        while True:
            try:
                return float(input("Digite o valor do produto: R$"))
            except ValueError:
                print("Valor inválido! Forneça um valor numerico com ou sem ponto flutuante\n")

    
    def change_product(self) -> None:
        while True:
            product_code: str = input("Digite o código do produto: ")
            
            if product_code == "cancel":
                return
            
            try:
                self.products_manager.get_product(product_code)
            except InexistentProductCodeError:
                print("Código de produto inválido!\n")
                continue
            
            while True:
                print("1. Alterar código do produto;")
                print("2. Alterar nome do produto;")
                print("3. Alterar valor do produto;")
                print("4. Sair")
                
                choice: str = input(">>> ")
                
                match choice:
                    case "1":
                        self.products_manager.update_product(
                            product_code,
                            updated_code=self.get_product_code()
                        )
                    
                    case "2":
                        self.products_manager.update_product(
                            product_code,
                            updated_name=self.get_product_name()
                        )
                    
                    case "3":
                        self.products_manager.update_product(
                            product_code,
                            updated_price=BRLMoney.parse_from_float(
                                self.get_product_price()
                            )
                        )
                    
                    case "4": break
                    
                    case _:
                        print("Opção inválida!")
    

    def register_product(self) -> None:
        print("Registrando novo produto...")
        
        code: str = self.get_product_code()
        name: str = self.get_product_name()
        price: float = self.get_product_price()
        
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
                            
            while True:
                confirmation: str = input(f"Deseja remover '{product.name}'?[s/n]: ")

                match confirmation:
                    case "s":
                        self.products_manager.unregister_product(code)
                        print(f"'{product.name}' foi removido com sucesso!")
                        return

                    case "n": break

                    case _:
                        print("Opção inválida!\n")

            clear_terminal()
    

    def show_products(self) -> None:
        print("Available products:")
        if not self.products_manager.products:
            print("No products available.")
            return

        count: int = 0

        while True:
            print("p - Previous")
            print("n - Next")
            print("q - Quit")
            print("- "*20)

            for product in list(self.products_manager.products.values())[count:count+5]:
                print(f"{list(self.products_manager.products.values()).index(product) + 1}. {product.code} - {product.name} ({self.products_manager.stock[product.code]}): {product.price}")

            command: str = input(">>> ")

            if command == "q":
                break

            elif command == "n" and count + 5 < len(self.products_manager.products):
                count += 5
            
            elif command == "p":
                count = max(0, count - 5)

            clear_terminal()


    def stock_product(self) -> None:
        print("Stocking a product...")
        code: str = input("Enter product code to stock: ")

        try:
            product: Product = self.products_manager.get_product(code)
            quantity: int = int(input(f"Enter quantity to stock for {product.name}: "))

            while True:
                print("Deseja incrementar ou definir do zero o estoque com o valor fornecido?")
                print("1 - incrementar\n2 - definir")
                choice: str = input(">>> ")

                match choice:
                    case "1":
                        self.products_manager.increase_stock(code, quantity)
                        break

                    case "2":
                        self.products_manager.set_stock(code, quantity)
                        break

                    case _:
                        print("Opção inválida\n")

            print(f"Stocked {quantity} units of {product.name}.")
        
        except InexistentProductCodeError:
            print(f"No product found with code {code}.")
    

    def run(self) -> None:
        print("-"*20, "Product Interface", "-"*20)

        while True:
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