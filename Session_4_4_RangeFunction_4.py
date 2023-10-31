# Prompt user for input
stop = int(input("Please enter an integer greater than 0: "))
print("%sHere are the even numbers between 0 and %d:"%
      ("\n"*5, stop))

# Loop through and print out even numbers
for num in range(0, stop + 1, 2):
    print(num)
