# User email and identification
user_email = "u@example.net"
user_id = "12345678"

# Get user input
user_input = "12345678"

# Assign boolean values to is_valid_email and is_valid_id
is_valid_email = user_input == user_email
is_valid_id = user_input == user_id

# Assign a boolean value to is_valid_input
is_valid_input = is_valid_email or is_valid_id

# Print is_valid_input to the shell
print(is_valid_input)
