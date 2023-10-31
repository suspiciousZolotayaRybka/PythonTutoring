# The break statement can exit a loop early
for i in range(1, 100, 4):
    print("i =", i)
    if (i == 25):
        # Break out of the loop before it reaches 100
        print("\n\nBreaking out of the loop now.")
        # "break out" of the loop
        break
