# Модель для товаров (ООП)
class Product:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

    @staticmethod
    def from_line(line: str):
        name, price = line.strip('—')
        return Product(name.strip(), int(price.strip()))

    def to_line(self):
        return f"{self.name} — {self.price}"
