word = input("Enter a silly word: ")
splice = input("Enter a few characters: ")

while (splice in word):
    print(splice, "is in", word)
    print()
    splice = input("Enter a few characters: ")

print(splice, "is not in", word)
