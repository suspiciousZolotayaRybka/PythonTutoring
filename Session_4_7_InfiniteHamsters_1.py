# Set food pellets equal to 10
food_pellets = 10

# While food pellets is greater than 0, hamster is eating
while True:
    print("Hamster is eating...", food_pellets, " food pellets remain.")
    food_pellets -= 1
    # If there are no food pellets, break the infinite loop
    if (food_pellets == 0):
        break
