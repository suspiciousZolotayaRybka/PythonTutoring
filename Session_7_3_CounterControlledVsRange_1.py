# Get the name and sales made for each day a shop was open
num_days = int(input("Enter the number of days: "))
days = []
daily_sales = []

print()
print("Enter data for the day(s) below.")
count = 0
while count < num_days:
    days.append(input("Enter the name of day #{}: ".format(count + 1)))
    daily_sales.append(float(input("Enter the sales for {}: ".format(days[count]))))
    count += 1

print()
print("Daily sales:")
count = 0
while count < len(days):
    print("%-10s $%.2f" % (days[count] + ":", daily_sales[count]))
    count += 1
