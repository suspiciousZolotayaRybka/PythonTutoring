original = "the morse code"
           #01234567890123
           #43210987654321

anagram_phrase = original[1]   # h
anagram_phrase += original[2]  # e
anagram_phrase += original[6]  # r
anagram_phrase += original[8]  # e
anagram_phrase += original[3]  # [space]
anagram_phrase += original[10] # c
anagram_phrase += original[5]  # o
anagram_phrase += original[4]  # m
anagram_phrase += original[-1] # e
anagram_phrase += original[-5] # [space]
anagram_phrase += original[-2] # d
anagram_phrase += original[-3] # o
anagram_phrase += original[0]  # t
anagram_phrase += original[-7] # s

print(anagram_phrase)

try:
    hamster = "S mores"
    hamster[1] = "'"
    print(hamster)
except (TypeError):
    print(hamster)
