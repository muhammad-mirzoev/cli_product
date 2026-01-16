# Модель для товаров (ООП)
class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    @staticmethod
    def from_line(line: str):
        line = line.replace("—", "-")
        parts = line.split("-")
        if len(parts) != 2:
            raise ValueError(f"Неправильная строка: {line}")
        return Product(parts[0].strip(), float(parts[1].strip()))

    def to_line(self):
        return f"{self.name} — {self.price}"
