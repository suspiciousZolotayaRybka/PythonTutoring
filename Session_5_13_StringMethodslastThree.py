def get_is_valid_name(name):
    # Name cannot have digits
    if name.replace(" ", "").isalpha():
        # Name should have one space
        if (name.count(" ") == 1):
            # The space should not come before or after the name
            if ((name.find(" ") != 0) and (name.find(" ") != len(name) - 1)):
                return True
    return False

def enter_name():
    is_entering_names = True
    while is_entering_names:
        name = input("Enter a name: ")
        is_valid_name = get_is_valid_name(name)
        if (is_valid_name):
            return name
        else:
            print("You did not enter a valid name.")
            print("Enter name in format [First Last]")

def main():
    name = enter_name()
    first_name = name[0:name.find(" ")]
    last_name = name[name.find(" ") + 1:len(name)]

    print("Name entered:", name)
    print("First Name:", first_name)
    print("Last Name:", last_name)
main()
