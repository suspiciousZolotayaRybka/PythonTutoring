# Get user input to determine value of is_program_running
is_user_logged_in = input("Is the user logged in?\nEnter True or False\n=>")
is_application_open = input("Is the application open?\nEnter True or False\n=>")

# Change user input to boolean
is_user_logged_in = eval(is_user_logged_in)
is_application_open = eval(is_application_open)

# Find and print is_program_running
is_program_running = is_user_logged_in and is_application_open
print("The program is running: %s" % (is_program_running))
