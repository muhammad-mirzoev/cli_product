# Вся логика проекта
from product import Product
from storage import Storage


class ProductManager:
    def __init__(self, filename):
        self.storage = Storage(filename)

    # Добавление продукта
    def add(self, name, price,):
        products = self.storage.read_all()
        products.append(Product(name, price))
        self.storage.write_all(products)

    # Обновление продукта
    def update(self, name, new_price):
        products = self.storage.read_all()
        for product in products:
            if product.name == name:
                product.price = new_price
        self.storage.write_all(products)

    # Удаление продукта
    def delete(self, name):
        products = self.storage.read_all()
        products = [p for p in products if p.name != name]
        self.storage.write_all(products)

    # Итог по всем продуктам
    def total(self):
        products = self.storage.read_all()
        return sum(p.price for p in products)
