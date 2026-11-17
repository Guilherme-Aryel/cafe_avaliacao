from models.managers.products_manager import ProductManager, Product
from utils import clear_terminal
from interfaces.base import SimpleInterface

class ShowProductsInterface(SimpleInterface):
    
    def __init__(self, products_manager: ProductManager) -> None:
        self.products_manager: ProductManager = products_manager
    
    
    def run(self) -> None:
        print("Available products:")
                
        if not self.products_manager.products:
            print("No products available.")
            return

        count: int = 0
        products: list[Product] = list(self.products_manager.products.values())
        previous_error_message: str | None = None

        while True:
            clear_terminal()
            print("="*40)
            print(" "*10, "Produtos")
            print("="*40)
            print("p - Previous")
            print("n - Next")
            print("q - Quit")
            print("- "*20)

            for product in products[count:count+5]:
                print("{}. {} - {} ({}): {}".format(
                        products.index(product) + 1,
                        product.code,
                        product.name,
                        self.products_manager.stock[product.code],
                        product.price
                    )
                )

            print("- "*20)
            
            if previous_error_message is not None:
                print(previous_error_message)
                previous_error_message = None
                print("- "*20)
            
            command: str = input(">>> ")
            
            match command:
                case "q": return

                case "n":
                    if count + 5 >= len(self.products_manager.products):
                        previous_error_message = "Não há próxima sessão"
                        continue
                    
                    count += 5
                    break
                
                case "p":
                    if count == 0:
                        previous_error_message = "Não há sessão anterior"
                        continue
                    
                    count -= 5
                    break
                
                case _: previous_error_message = "Opção inválida!"
    