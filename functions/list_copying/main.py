# List of product prices
product_prices = [1.50, 2.50, 3.00, 0.99, 2.30]

def apply_discount(prices):
    prices_copy = product_prices.copy()
    for n in range(len(prices_copy)):
        if prices_copy[n] > 2:
            prices_copy[n] = prices_copy[n]*0.9
    return(prices_copy)

# Call the function and store the updated prices
updated_prices = apply_discount(product_prices)

for n in updated_prices:
    l = int(n)
    print("Updated product prices: $"+str(updated_prices[l]))
