# Prompt user for the temperature and weather status
temperature = input('''Please enter the temperature
=>''')
is_raining = input('''Is it raining (True/False)
=>''')

# Type convert variables
temperature = float(temperature)
is_raining = eval(is_raining)

# If it is not raining and a good temperature is_pool_open is True
is_pool_open = not(is_raining) and (70 < temperature < 100)

print(f"The pool is open: {is_pool_open}")
