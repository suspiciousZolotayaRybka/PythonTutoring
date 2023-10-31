def print_menu():
    print('''
1. Add Weekly Sales
2. Change Weekly Sales
3. Print Weekly Sales
9. Exit Program
''')

def get_user_choice():
    user_choice = input("Enter your choice.\n=>")
    if (user_choice == "1"):
        return 1
    elif(user_choice == "2"):
        return 2
    elif (user_choice == "3"):
        return 3
    elif (user_choice == "9"):
        return 9
    else:
        print("Invalid Input")
        return -1

def add_weekly_sales(days, daily_sales):
    # TODO
    print("Placeholder for add_weekly_sales()")
    input("Press ENTER to continue...")
    print("\n"*25)

def change_weekly_sales(days, daily_sales):
    # TODO
    print("Placeholder for change_weekly_sales()")
    input("Press ENTER to continue...")
    print("\n"*25)

def print_weekly_sales(days, daily_sales):
    # TODO
    print("Placeholder for print_weekly_sales()")
    input("Press ENTER to continue...")
    print("\n"*25)

def main():
    # Assign variables
    days = []
    daily_sales = []
    program_running = True

    print("Welcome to the weekly sales tracker!")
    while (program_running):
        print_menu()
        c = get_user_choice()
        if (c == 1):
            add_weekly_sales(days, daily_sales)
        elif (c == 2):
            change_weekly_sales(days, daily_sales)
        elif (c == 3):
            print_weekly_sales(days, daily_sales)
        elif (c == 9):
            program_running = False
    print("Thank you for using the weekly sales tracker!")

main()
'''

    sales_string = ""
    if (len(days) == 0):
        sales_string = ""
    else:
        for day in days:
            sales_string = f"{day}: {daily_sales[days.index(day)]}\n"

    '''
