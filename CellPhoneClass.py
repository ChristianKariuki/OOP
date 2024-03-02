import random

class CellPhone:
    
    def __init__(self):
        self.manufact, self.model = self.random_manufact_and_model()
        self.retail_price = self.random_retail_price()

    def random_manufact_and_model(self):
        manufacturers = ['Apple', 'Samsung', 'Google', 'OnePlus']
        models = {'Apple': ['iPhone 13', 'iPhone 12', 'iPhone 11'],
                  'Samsung': ['Galaxy S21', 'Galaxy S20', 'Galaxy Note'],
                  'Google': ['Pixel 6', 'Pixel 5', 'Pixel 4']}
        chosen_manufact = random.choice(manufacturers)
        chosen_model = random.choice(models[chosen_manufact])
        return chosen_manufact, chosen_model

    def random_retail_price(self):
        return random.randint(500, 1000)

    def get_manufact(self):
        return self.manufact

    def get_model(self):
        return self.model

    def get_retail_price(self):
        return self.retail_price

