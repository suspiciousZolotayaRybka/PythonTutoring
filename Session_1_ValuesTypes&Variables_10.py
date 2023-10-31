string_variable = "rounded to the nearest hundredth is"
integer_variable = 2
float_variable = 2.555
sum_of_variables = integer_variable + float_variable

print(integer_variable, "+", float_variable, string_variable, sum_of_variables)

print("%d + %.3f %s %.2f" % (integer_variable, float_variable, string_variable, sum_of_variables))

print(f"{integer_variable:d} + {float_variable:.3f} {string_variable:s} {sum_of_variables:.2f}")

print(f"""{integer_variable:d} + {float_variable:.3f} {string_variable:s}:
{sum_of_variables:.2f}""")
