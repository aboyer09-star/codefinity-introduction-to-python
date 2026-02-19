# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}
# "Item": [current stock, minimum stock, 
#restock quantity, on sale (True/False)]
dt = 100

print("Processing started!")

for n in inventory: #if stock is < minimum, add refill
    f = inventory.get(n)
    print("Processing " + n)
    while f[0] < f[1]:
        f[0] += f[2]
    if (f[0] > dt) and f[3]==False:
        f[3]=True

print("Processing completed!")