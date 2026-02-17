prices = [29.99, 45.50, 12.75, 38.20]

for n in range(len(prices)):
    if n==0:
        prices[n] -= 0.1*prices[n]
        print(f"Update price for item {n}: ${prices[n]:.2f}")
    
    elif n==1:
        prices[n] -= 0.2*prices[n]
        print(f"Update price for item {n}: ${prices[n]:.2f}")
    
    elif n==2:
        prices[n] -= 0.15*prices[n]
        print(f"Update price for item {n}: ${prices[n]:.2f}")
        
    elif n==3:
        prices[n] -= 0.05*prices[n]
        print(f"Update price for item {n}: ${prices[n]:.2f}")

