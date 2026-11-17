from interfaces.base import SimpleInterface
from interfaces.confirmation import YNConfirmationInterface
from models.managers.products_manager import (
    ProductManager,
    Product
)
from interfaces.products.sub.product_getters import ProductGetters
from models.money.brl_money import BRLMoney


class RegisterProductInterface(SimpleInterface):
    
    def __init__(
        self,
        products_manager: ProductManager,
        product_getters: ProductGetters
    ) -> None:
        
        self.products_manager: ProductManager = products_manager
        self.confirmation: YNConfirmationInterface = YNConfirmationInterface("s")
        self.product_getters: ProductGetters = product_getters
    
    
    def run(self) -> None:
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