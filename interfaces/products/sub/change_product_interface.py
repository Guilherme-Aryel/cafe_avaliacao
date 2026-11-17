from models.managers.products_manager import ProductManager, InexistentProductCodeError
from interfaces.products.sub.product_getters import ProductGetters
from interfaces.base import SimpleInterface
from models.money.brl_money import BRLMoney


class ChangeProductInterface(SimpleInterface):
    
    def __init__(self, products_manager: ProductManager, product_getters: ProductGetters) -> None:
        self.products_manager: ProductManager = products_manager
        self.product_getters: ProductGetters = product_getters
    
    
    def run(self) -> None:
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
                            updated_code=self.product_getters.get_product_code()
                        )
                    
                    case "2":
                        self.products_manager.update_product(
                            product_code,
                            updated_name=self.product_getters.get_product_name()
                        )
                    
                    case "3":
                        self.products_manager.update_product(
                            product_code,
                            updated_price=BRLMoney.parse_from_float(
                                self.product_getters.get_product_price()
                            )
                        )
                    
                    case "4": break
                    
                    case _:
                        print("Opção inválida!")