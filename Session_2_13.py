'''
If the if part executes first,
the variable "message" will not be visible at the end of the program.
'''

some_condition = True
if (some_condition):
    print(some_condition)
else:
    message = "some_condition was false!"

print(message)
