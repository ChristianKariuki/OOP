import random

class Car:
    def __init__(self):
        self.year_model = random.randint(2014, 2024)  
        self.make = 'Toyota'  
        self.speed = 0        

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5
        self.speed = max(0, self.speed)  

    def getSpeed(self):
        return self.speed
