from typing import cast

from models.product import Product
from models.json_handler import JSONHandler
from errors.product import InexistentProductCodeError

class ProductManager:

    def __init__(self, json_handler: JSONHandler) -> None:
        self.json_handler: JSONHandler = json_handler
        self.products_data: dict[str, dict[str, str | float | int]] = self.json_handler.read_json(default={})
        self.products: dict[str, Product] = self.parse_products(self.products_data)
        self.stock: dict[str, int] = {code: cast(int, product["quantity"]) for code, product in self.products_data.items()}
    

    def parse_products(self, products_data: dict[str, dict[str, str | float | int]]) -> dict[str, Product]:
        return {
            code: Product.from_dict(product_data)
            for code, product_data in products_data.items()
        }
    

    def get_product(self, product_code: str) -> Product:
        if product_code not in self.products:
            raise InexistentProductCodeError(product_code)
        
        return self.products[product_code]


    def stock_product(self, product_code: str, quantity: int) -> None:
        if product_code not in self.products:
            raise InexistentProductCodeError(product_code)
        
        self.stock[product_code] += quantity


    def register_product(self, product: Product) -> None:
        self.products[product.code] = product
        self.json_handler.write_json({
            code: product.to_dict()
            for code, product in self.products.items()
        })


    def unregister_product(self, product_code: str) -> None:
        if product_code not in self.products:
            raise InexistentProductCodeError(product_code)
        
        del self.products[product_code]

        self.json_handler.write_json({
            code: product.to_dict()
            for code, product in self.products.items()
        })