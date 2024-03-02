import random

class Retail:
    def __init__(self):
        self.items = [
            self.create_item('Jacket', 12, 59.95),
            self.create_item('Designer Jeans', 40, 34.95),
            self.create_item('Shirt', 20, 24.95)
        ]

    def create_item(self, description, units, price):
        return {'description': description, 'units': units, 'price': price}
