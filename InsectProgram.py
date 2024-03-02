import InsectClass as i


mosquito = i.insect()
housefly = i.insect()

mosquito.calc_flight()
housefly.calc_flight()

print(f"the mosquito can travel up to {mosquito.get_miles()} miles")
print(f"the housefly can travel up to {housefly.get_miles()} miles")