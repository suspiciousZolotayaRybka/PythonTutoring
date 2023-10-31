# Assign a list of hamsters
hamsters = ["Nibbles", "S'mores", "Mochi", "Peanut", "Sprinkles"]

# Ask the shop if they have a hamster
print("What hamster would you like to ask about?")
hamster = input("=>")

# See if the shop has the hamster
if (hamster in hamsters):
    print("Yes, we have", hamster, "waiting for a new home!")
else:
    print("Sorry,", hamster, "is not one of our hamsters at the moment.")
