import CarClass as cc

my_car = cc.Car()

print(f"Car Year Model: {my_car.year_model}")
print(f"Car Make: {my_car.make}")

for _ in range(5):
    my_car.accelerate()
    print(f"Current speed after accelerating: {my_car.getSpeed()} km/h")

for _ in range(5):
    my_car.brake()
    print(f"Current speed after braking: {my_car.getSpeed()} km/h")
