# Get the name and sales made for each day a shop was open
num_days = int(input("Enter the number of days: "))
days = []
daily_sales = []

print()
print("Enter data for the day(s) below.")
for i in range(num_days):
    days.append(input("Enter the name of day #{}: ".format(i + 1)))
    daily_sales.append(float(input("Enter the sales for {}: ".format(days[i]))))

print()
print("Daily sales:")
for i in range(len(days)):
    print("%-10s $%.2f" % (days[i] + ":", daily_sales[i]))
