# This program gets a positive one-digit integer and displays its Roman numeral

def greet_user():
    # Get the user's name
    name = input("Please enter your name: ")
    # Greet the user
    print(f"Hello, {name}!")

def find_valid_input():
    # Get the user's favorite positive one-digit number
    positive_one_digit_integer = input("Please enter your favorite number between 1-9\n=>")
    # Assign important variables then check to see if the user's number is 1-9
    num = positive_one_digit_integer
    if (num == '1' or num == '2' or num == '3' or num == '4' or num == '5'
        or num == '6' or num == '7' or num == '8' or num == '9'):
        print(positive_one_digit_integer, "is a valid positive one-digit integer!")
        num = int(positive_one_digit_integer)
        return num
    else:
        print(positive_one_digit_integer, "is not between 1-9. Please try again.")
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
    
    # If num is returned as -1, user's input was invalid
    num = find_valid_input()
    
    if (num != -1):
        greet_user()
        print_roman_numeral(num)

main()
