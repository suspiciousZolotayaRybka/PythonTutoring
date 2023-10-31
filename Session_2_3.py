# Prompt the user to enter an integer
variable_1 = input('''Please enter an integer
=>''')
# Type convert variable_2 into an integer
variable_2 = int(variable_1)
# Assign variable_3 and variable_4
variable_3 = variable_2 == variable_1
variable_4 = 1 == '1'

output = f'''Value of variable_3: {variable_3}
Value of variable_4: {variable_4}'''
print(output)
