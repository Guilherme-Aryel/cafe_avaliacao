from collections.abc import Callable
from time import sleep

from interfaces.base import Interface
from models.managers.products_manager import ProductManager
from interfaces.confirmation import YNConfirmationInterface
from utils import clear_terminal

from interfaces.products.sub.show_products_interface import ShowProductsInterface
from interfaces.products.sub.change_product_interface import ChangeProductInterface
from interfaces.products.sub.stock_product_interface import StockProductInterface
from interfaces.products.sub.unregister_product_interface import UnregisterProductInterface
from interfaces.products.sub.register_products_interface import RegisterProductInterface
from interfaces.products.sub.product_getters import ProductGetters


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
        
        self.stock_product_interface: StockProductInterface = StockProductInterface(
            self.products_manager, self.product_getters
        )
        
        self.unregister_product_interface: UnregisterProductInterface = UnregisterProductInterface(
            self.products_manager
        )
        
        self.register_product_interface: RegisterProductInterface = RegisterProductInterface(
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
        self.register_product_interface.run()


    def unregister_product(self) -> None:
        self.unregister_product_interface.run()


    def show_products(self) -> None:
        self.show_products_interface.run()
    
    
    def stock_product(self) -> None:
        self.stock_product_interface.run()
                           

    def run(self) -> None:
        while True:
            self.show_title()
            self.show_options()
            entry: str = input(">>> ")

            if entry == "sair":
                return

            if entry in self.command_dispatch:
                clear_terminal()
                self.command_dispatch[entry]()
                sleep(1)
                clear_terminal()
            else:
                print("Comando inválido! Tente novamente.")