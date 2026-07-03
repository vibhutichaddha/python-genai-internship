class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    @property
    def price (self):
        return self._price
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value
p=Product("Laptop", 60000)
print("Product:",p.name)
print("Price:",p.price)
p.price=65000