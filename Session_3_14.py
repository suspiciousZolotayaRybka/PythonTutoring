# Concatenate bananas to banana_string
def concatenate_bananas(banana_string):
    banana_string = banana_string + " bananas"
    return banana_string

# Pass user input into concatenate_bananas()
user_input = input("Please enter an argument: ")
result = concatenate_bananas(user_input)
result = result + "!"
print(result)
