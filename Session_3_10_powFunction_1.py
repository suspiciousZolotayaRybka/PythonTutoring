import math

# Using the ** operator
exponential_result_1 = 2**2**3
# pow as a built-in function vs pow from the math library
exponential_result_2 = pow(2, math.pow(2, 3))

# Print out the results
print("exponential_result_1:", exponential_result_1)
print("exponential_result_2:", exponential_result_2)
