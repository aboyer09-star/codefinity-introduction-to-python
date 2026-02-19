# Inventory dictionary with stock, price, and discount price
inventory = {
    "Bread": [42, 1.20, 0.99],  # "Item": [current stock, regular price, 
    #discounted price]
    "Eggs": [225, 2.12, 1.99],  # Eggs should be sold at a discount
    "Apples": [9, 1.50, 1.35]   # Apples need to be restocked
}

for n in inventory:
    i = inventory.get(n)
    r = i[1]
    d= i[2]
    if i[0] < 30:
        print(f"{n} need restocking.")

    elif 30 <= i[0] <= 100:
        print(f"{n} should be sold at the regular price of {r}.")

    else:
        print(f"{n} should be sold at the discounted price of {d}.")
