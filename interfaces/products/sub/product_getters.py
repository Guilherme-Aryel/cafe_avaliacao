from models.managers.products_manager import (
    Product,
    ProductManager,
    InexistentProductCodeError
)


class ProductGetters:
    
    def __init__(self, products_manager: ProductManager) -> None:
        self.products_manager: ProductManager = products_manager
    
    
    def get_product_by_code(self) -> Product:
        while True:
            code: str = input("Digite o código do produtor: ")

            try:
                return self.products_manager.get_product(code)
            except InexistentProductCodeError:
                print(f"Nenhum produto encontrado com o código: {code}.")
                continue
    
    
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
    