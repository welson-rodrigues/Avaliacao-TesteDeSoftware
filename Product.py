class Product:
    id : int
    name : str
    price : float
    stock : int

    def __init__(self, id, name, stock, price):
        self.id = id
        self.name = name
        self.stock = stock
        self.price = price

    def increase_stock(self, quantity: int):
        self.check_positive_number(quantity)
        self.stock: int = self.stock + quantity

    def decrease_stock(self, quantity: int):
        self.check_positive_number(quantity)
        new_stock = self.stock - quantity
        self.check_negative_stock(new_stock)
        self.stock = new_stock

    def check_negative_stock(self, value):
        if value < 0:
            raise Exception('O estoque deve ser positivo')

    def check_positive_number(self, value):
        if value <= 0:
            raise Exception('O número deve ser positivo')


# test_nomedometodoasertestado