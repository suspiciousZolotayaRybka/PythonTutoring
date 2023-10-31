# Prompt user for a number greater than zero
num = int(input('''Please enter a number greater than 0
=>'''))

# Show the integer division of three between 0 and num
while (num >= 0):
    print(f"{num}//3 = {num//3}")
    # Print a line break between each floor division group
    if (num % 3 == 0):
        print()
    num -= 1
          
