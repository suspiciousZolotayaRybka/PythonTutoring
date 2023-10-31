word1 = (input("Enter word 1: ")).lower()
word2 = (input("Enter word 2: ")).lower()

if (word1 < word2):
    print(word1, "comes before", word2)
elif (word1 == word2):
    print(word1, "is the same as", word2)
else:
    print(word2, "comes before", word1)
