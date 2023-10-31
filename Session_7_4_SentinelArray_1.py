days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
daily_sales = [532.15, 775.43, 613.26, 439.76, 541.78]

day = "Monday"
print("Enter a day to view its sales.")
print("Enter anything else to exit.")
while (day in days):
    print()
    day = input("Enter a day: ")
    if (day in days):
        sales = daily_sales[days.index(day)]
        print("{} sales: {:.2f}".format(day, sales))
