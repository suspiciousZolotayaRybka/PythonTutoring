# Take user input using type casting functions
# str() can be used to type cast to string, but all input is string by default
string_variable = input("1 => ")
# Type casting functions include int(), float(), and bool()
integer_variable = input("2 => ")
integer_variable = int(integer_variable)
float_variable = input("3 => ")
float_variable = float(float_variable)
boolean_variable = input("4 => ")
boolean_variable = bool(boolean_variable)

# Print the types for user input
print("String variable: ", type(string_variable))
print("Integer variable: ", type(integer_variable))
print("Float variable: ", type(float_variable))
print("Boolean variable: ", type(boolean_variable))
