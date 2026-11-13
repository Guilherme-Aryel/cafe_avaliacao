from collections.abc import Callable
from time import sleep

from errors.product import InexistentProductCodeError
from interfaces.base import Interface
from models.money.brl_money import BRLMoney
from models.product import Product
from models.products_manager import ProductManager
from utils import clear_terminal


class ProductInterface(Interface):

    def __init__(self, products_manager: ProductManager) -> None:
        super().__init__(accepted_permissions=["admin"])

        self.products_manager: ProductManager = products_manager
        self.command_dispatch: dict[str, Callable[[], None]] = {
            "register": self.register_product,
            "unregister": self.unregister_product,
            "stock_product": self.stock_product,
            "show": self.show_products,
            "exit": lambda: None
        }


    def show_options(self) -> None:
        print("Available commands:")
        for command in self.command_dispatch.keys():
            print(f"- {command}")


    def get_product_code(self) -> str:
        while True:
            code: str = input("Enter product code: ")

            if code: return code

            print("Valor inválido! Digite algum valor para ser o código do produto\n")


    def get_product_name(self) -> str:
        while True:
            name: str = input("Enter product name: ")

            if name: return name

            print("Valor inválido! Digite algum valor para ser o código do produto\n")


    def get_product_price(self) -> float:
        while True:
            try:
                return float(input("Enter product price: "))
            except ValueError:
                print("Valor inválido! Forneça um valor numerico\n")


    def register_product(self) -> None:
        print("Registering a new product...")
        
        code: str = self.get_product_code()
        name: str = self.get_product_name()
        price: float = self.get_product_price()
        
        product: Product = Product(
            code,
            name,
            price=BRLMoney.parse_from_float(price)
        )

        self.products_manager.register_product(product)
        print(f"Product {product.name} registered successfully!")


    def unregister_product(self) -> None:
        print("Unregistering a product...")
        code: str = input("Enter product code to unregister: ")
        try:
            self.products_manager.unregister_product(code)
            print(f"Product with code {code} unregistered successfully!")
        except InexistentProductCodeError as e:
            print(e)


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