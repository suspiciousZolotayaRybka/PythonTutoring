full_name = "Benjamin Kozak"
first_initial = full_name[0]
count = 0
for letter in full_name:
    if letter == chr(32):
        last_initial = full_name[count + 1]
    count += 1

print(first_initial, last_initial)
