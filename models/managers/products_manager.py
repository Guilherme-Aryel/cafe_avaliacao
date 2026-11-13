from typing import cast

from models.dataclasses.product import Product
from services.json_handler import JSONHandler
from errors.product import InexistentProductCodeError


class ProductManager:

    def __init__(self, json_handler: JSONHandler) -> None:
        self.json_handler: JSONHandler = json_handler
        self.products_data: dict[str, dict[str, str | float | int]] = self.json_handler.read_json(default={})
        self.products: dict[str, Product] = self.parse_products(self.products_data)
        self.stock: dict[str, int] = {code: cast(int, product["quantity"]) for code, product in self.products_data.items()}


    @property
    def product_codes(self) -> list[str]:
        return list(self.products.keys())


    def parse_products(self, products_data: dict[str, dict[str, str | float | int]]) -> dict[str, Product]:
        return {
            code: Product.from_dict(product_data)
            for code, product_data in products_data.items()
        }
    

    def get_product(self, product_code: str) -> Product:
        if product_code not in self.products:
            raise InexistentProductCodeError(product_code)
        
        return self.products[product_code]


    def get_product_by_name(self, product_name: str) -> Product | None: 
        for product in self.products.values():
            if product.name == product_name:
                return product


    def update_products_db(self) -> None:
        self.json_handler.write_json({
            code: product.to_dict() | { "quantity" : self.stock[product.code] }
            for code, product in self.products.items()
        })


    def increase_stock(self, product_code: str, quantity: int) -> None:
        if product_code not in self.products:
            raise InexistentProductCodeError(product_code)
        
        self.stock[product_code] += quantity


    def set_stock(self, product_code: str, quantity: int) -> None:
        if product_code not in self.products:
            raise InexistentProductCodeError(product_code)
        
        self.stock[product_code] = quantity


    def register_product(self, product: Product) -> None:
        self.products[product.code] = product
        self.set_stock(product.code, 0)
        self.update_products_db()


    def unregister_product(self, product_code: str) -> Product:
        if product_code not in self.products:
            raise InexistentProductCodeError(product_code)

        product: Product = self.products[product_code]

        del self.products[product_code]
        del self.stock[product_code]

        self.update_products_db()

        return product