# Assign hamsters and food_pellets
hamsters = ["Nibbles", "S'mores", "Mochi",
            "Peanut", "Sprinkles"]
food_pellets = 5

print("""Welcome to the Hamster Diet Program.
%s
Please press ENTER for every food pellet eaten.%s"""%
      ("="*36, "\n"*2))

# Iterate through each hamster
for hamster in hamsters:
    print("Current hamster", hamster, "is eating.")
    # Use input to manually keep track of progress
    while (food_pellets > 0):
        input(str(food_pellets) + " food pellets remaining")
        food_pellets -= 1
    # Exit the while loop, current hamster has finished
    print(hamster, " finished eating.\n")
    food_pellets = 5
