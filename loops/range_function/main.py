# List of products on promotion for each weekday
daily_promotions = ["Milk", "Eggs", "Bread", "Apples", "Oranges"]

# List of weekdays corresponding to the promotions
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

for n in range(len(weekdays)):
    weekday = weekdays[n]
    promotion = daily_promotions[n]
    print(weekday+": Promotion on "+ promotion)