import CellPhoneClass as cp

phone1 = cp.CellPhone()
phone2 = cp.CellPhone()

print(f"The first phone is a {phone1.get_manufact()} {phone1.get_model()} priced at ${phone1.get_retail_price()}")
print(f"The second phone is a {phone2.get_manufact()} {phone2.get_model()} priced at ${phone2.get_retail_price()}")
