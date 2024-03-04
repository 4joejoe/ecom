from django.shortcuts import render


class Product:
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        sku: str,
        category: str,
        brand: str,
        stock_quantity: int,
        weight: float,
        dimensions: str,
        seo_name: str,
    ) -> None:

        self.name = name
        self.description = description
        self.price = price
        self.sku = sku
        self.category = category
        self.brand = brand
        self.stock_quantity = stock_quantity
        self.weight = weight
        self.dimensions = dimensions
        self.seo_name = seo_name

    def change_name(self, new_name: str) -> str:
        self.name = new_name
        return self.name

    def change_description(self, new_description: str) -> str:
        self.description = new_description
        return self.description

    def change_price(self, new_price: float) -> float:
        self.price = new_price
        return self.price

    def change_sku(self, new_sku: str) -> str:
        self.sku = new_sku
        return self.sku

    def change_category(self, new_category: str) -> str:
        self.category = new_category
        return self.category

    def change_brand(self, new_brand: str) -> str:
        self.brand = new_brand
        return self.brand

    def change_stock_quantity(self, new_stock_quantity: int) -> int:
        self.stock_quantity = new_stock_quantity
        return self.stock_quantity

    def change_weight(self, new_weight: float) -> float:
        self.weight = new_weight
        return self.weight

    def change_dimensions(self, new_dimensions: str) -> str:
        self.dimensions = new_dimensions
        return self.dimensions

    def change_seo_name(self, new_seo_name: str) -> str:
        self.seo_name = new_seo_name
        return self.seo_name

    def __str__(self) -> str:
        return f"{self.name} - {self.price}"
