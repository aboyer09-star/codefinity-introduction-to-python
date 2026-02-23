# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}
total_sales_list = []

for n in products:
    list = products.get(n)
    f_list = float(list[0])
    int_q = int(list[1])
    total_sales = f_list * int_q
    print("Total sales for "+n+": $"+str(total_sales))
    total_sales_list.append(total_sales)

total_sum = sum(total_sales_list)
min_sales = min(total_sales_list)
max_sales = max(total_sales_list)

print("Total sum of all sales: $"+str(total_sum))
print("Minimum sales: $"+str(min_sales))
print("Maximum sales: $"+str(max_sales))