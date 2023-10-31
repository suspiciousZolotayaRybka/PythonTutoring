sum_animals = 24
animal_names = "kittens & puppies"

# Triple quotes and string formatting with placeholders
print("""There are %d %s at the animal shelter.
.
.
.
.
.
Take your pick!""" % (sum_animals, animal_names))

# Triple quotes and f-strings
print(f"""There are {sum_animals} {animal_names} at the animal shelter.
.
.
.
.
.
Take your pick!""")

# Single quotes and formatting with placeholders
print("There are %d %s at the animal shelter%sTake your pick!" % (sum_animals, animal_names, ".\n"*6))

# Single quotes and f-strings
line_breaks = ".\n"*6
print(f"There are {sum_animals} {animal_names} at the animal shelter.{line_breaks}Take your pick!")
