import random

# Assign variables
random_number = random.randrange(1, 20)
user_input = 0

# Allow user to guess the number or enter -1 to exit the loop
while (user_input != -1):
    # Prompt the user
    user_input = int(input("Guess a number between 1-20 or enter -1 to quit: "))
    print("\n"*5)
    # Tell the user whether or not their number was correct
    if (user_input == random_number):
        print("You guessed correct.\nCongratulations!")
        # Their number was correct, so exit the loop
        user_input = -1
    elif (user_input == -1):
        # The user entered -1 to exit
        print("You chose to exit")
    else:
        # The user did not guess correctly
        print("Sorry, that was incorrect.")

