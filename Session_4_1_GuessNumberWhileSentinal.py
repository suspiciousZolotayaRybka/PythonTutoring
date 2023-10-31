# Assign variables
sentinel_value = -1
random_number = 15
user_input = 0

# Control a while loop that allows the user to guess
while (user_input != sentinel_value):
    # Prompt the user
    user_input = int(input("Guess a number between 1-20 or enter -1 to quit: "))
    print("\n"*5)
    # Tell the user whether or not their number was correct
    if (user_input == random_number):
        print("You guessed correct.\nCongratulations!")
        # Their number was correct, so exit the loop
        user_input = -1
    elif (user_input == sentinel_value):
        # The user entered -1 to exit
        print("You chose to exit")
    else:
        # The user did not guess correctly
        print("Sorry, that was incorrect.")

