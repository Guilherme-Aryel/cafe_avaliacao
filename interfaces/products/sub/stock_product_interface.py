from interfaces.base import SimpleInterface
from interfaces.products.sub.product_getters import ProductGetters, Product, ProductManager


class StockProductInterface(SimpleInterface):
    
    def __init__(
        self,
        products_manager: ProductManager,
        product_getters: ProductGetters
    ) -> None:
        
        self.product_getters: ProductGetters = product_getters
        self.products_manager: ProductManager = products_manager
    
    
    def get_quantity(self) -> int:
        while True:
            try:
                return int(input(
                    f"Digite a quantidade de produtos que deseja estocar: ")
                )
            except ValueError:
                print("Digite um valor númerico!\n")
                continue
    
    
    def run(self) -> None:
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