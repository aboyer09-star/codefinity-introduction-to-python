def apply_discount(price, discount = 0.05):
    price = float(price) * (1-discount)
    return price

def apply_tax(price, tax = 0.07):
    price = float(price) * (1+tax)
    return price

def calculate_total(price, discount = 0.05, tax = 0.07):
    new_price = apply_tax(apply_discount(price, discount), tax)
    return new_price


default = calculate_total(120)
custom = calculate_total(100, discount = 0.10, tax = 0.08)

print("Total cost with default discount and tax: $"+str(default))
print("Total cost with custom discount and tax: $"+str(custom))







