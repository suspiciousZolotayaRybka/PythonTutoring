word = input("Please enter a silly word: ")
splice = input("Please enter a few characters: ")

if (splice in word):
    print(splice, "is in", word)
else:
    print(splice, "is not in", word)
