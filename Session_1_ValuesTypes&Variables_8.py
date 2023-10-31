# Take user input using the eval() function
string_variable = input("1 => ")
# Eval cannot be used for string variables that don't contain a valid expression
# For example, eval("hello world") would throw an error
integer_variable = input("2 => ")
integer_variable = eval(integer_variable)
float_variable = input("3 => ")
float_variable = eval(float_variable)
boolean_variable = input("4 => ")
boolean_variable = eval(boolean_variable)

# Print the types for user input
print("String variable: ", type(string_variable))
print("Integer variable: ", type(integer_variable))
print("Float variable: ", type(float_variable))
print("Boolean variable: ", type(boolean_variable))
