print("ASCII table for values 97-122")
print("=============================")
print("Decimal Value: ", end="")
for i in range(97, 123):
    print("%-4d"%(i), end="")
print()
print("Character:     ", end="")
for i in range(97, 123):
    print("%-4s"%(chr(i)), end="")
    
