# Ask the user if they want to continue
user_choice = input('''Enter "yes" to continue... 
\t=>''')

# Determine whether or not the user entered yes
if (user_choice.upper() == 'YES'):
    print("You chose to continue")
else:
    print("You chose not to continue")
