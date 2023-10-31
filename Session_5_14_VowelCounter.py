vowels = 'aeiou'
vowel_count = 0
a_count = 0
e_count = 0
i_count = 0
o_count = 0
u_count = 0

word = (input("Enter a word: ")).lower()

# Count the number of vowels
for letter in word:
    if letter in vowels:
        vowel_count += 1
        if letter == 'a':
            a_count += 1
        elif letter == 'e':
            e_count += 1
        elif letter == 'i':
            i_count += 1
        elif letter == 'o':
            o_count += 1
        else:
            u_count += 1
        
print("{} has {:d} vowels.".format(word,
                                   vowel_count))
print("""a: {:5d}
e: {:5d}
i: {:5d}
o: {:5d}
u: {:5d}""".format(a_count,
                   e_count,
                   i_count,
                   o_count,
                   u_count))

    
