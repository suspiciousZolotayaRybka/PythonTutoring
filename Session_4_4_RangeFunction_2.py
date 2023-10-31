values = []
index = 0
for i in range(97, 124):
    values.append(chr(i))
    index += 1

items_string = ""
num_string = ""

num = 97
for item in values:
    num_string += str(num) + " "
    if num < 100:
        items_string += str(item) + "  "
    else:
        items_string += str(item) + "   "
    num += 1
print("ASCII table for values 97-123\n%s\nDecimal Value:%s\nASCII Value:  %s"%
      ("=" * 29, num_string, items_string))
