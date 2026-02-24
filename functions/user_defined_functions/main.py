# Call the function and print the result

def calculate_total_cost(price, quantity):
    t_cost = price * quantity
    return(t_cost)

apples_total_cost = calculate_total_cost(1.50, 10)

print("The total cost for apples is $"+str(apples_total_cost))


