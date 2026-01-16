# Работа с файлом
from product import Product


class Storage:
    def __init__(self, filename: str):
        self.filename = filename

    def read_all(self):
        products = []
        try:
            with open(self.filename, "r", encoding='utf=8') as f:
                for line in f:
                    if line.strip():
                        products.append(Product.from_line(line))
        except FileNotFoundError:
            pass
        return products

    def write_all(self, products):
        with open(self.filename, "w", encoding='utf=8') as f:
            for product in products:
                f.write(product.to_line() + "\n")
