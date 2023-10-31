# Assign user_email and user_id
user_email = "u@example.net"
user_id = "12345678"

# Use the input() function to get user_input
user_input = input("Please enter your id or email.\n=>")

# Assign a boolean value to is_valid_input based on id and email
is_valid_input = (user_input == user_id) or (user_input == user_email)

# Inform the user whether or not their input was valid
if (is_valid_input):
    print("%s was valid input. Access was granted." % (user_input))
else:
    print("You entered an invalid id or email.\nPlease try again.")
