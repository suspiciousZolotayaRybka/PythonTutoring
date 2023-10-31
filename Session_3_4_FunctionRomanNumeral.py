# This program gets a positive one-digit integer and displays its Roman numeral

def greet_user():
    # Get the user's name
    name = input("Please enter your name: ")
    # Greet the user
    print(f"Hello, {name}!")

def find_valid_input():
    # Get the user's favorite positive one-digit number
    num = input("Please enter your favorite number between 1-9\n=>")
    # Check to see if the user's number is 1-9
    if (num == '1' or num == '2' or num == '3' or num == '4' or num == '5'
        or num == '6' or num == '7' or num == '8' or num == '9'):
        print(num, "is a valid positive one-digit integer!")
        num = int(num)
        return num
    else:
        return -1

def print_roman_numeral(num):
    # Tell the user what their number as a Roman numeral is
    if(num == 1):
        roman_numeral = 'I'
    elif(num == 2):
        roman_numeral = 'II'
    elif(num == 3):
        roman_numeral = 'III'
    elif(num == 4):
        roman_numeral = 'IV'
    elif(num == 5):
        roman_numeral = 'V'
    elif(num == 6):
        roman_numeral = 'VI'
    elif(num == 7):
        roman_numeral = 'VII'
    elif(num == 8):
        roman_numeral = 'VIII'
    else:
        roman_numeral = 'IX'
    print("%d as a roman numeral is %s" % (num, roman_numeral))

def main():

    greet_user()
    
    # If num is returned as -1, user's input was invalid
    num = find_valid_input()

    if (num != -1):
        print(f"{num} squared is", math.pow(num, 2))

main()
