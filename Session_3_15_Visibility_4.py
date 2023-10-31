# Define function return_hello_string()
def assign_hello_string():
    global hello_string
    hello_string = "Hello World"

def main():
    # Call function return_hello_string()
    assign_hello_string()
    print(hello_string)
main()
