# Define main()
def main():
    # Prompt the user for color information
    color = input("Please enter your favorite color (BLUE/YELLOW/GREEN):")

    # Assign message based on the users favorite color
    if (color == 'BLUE'):
        message = "Blue is a nice color.\nIt is the color of the ocean."
    elif (color == 'YELLOW'):
        message = "Yellow is a nice color.\nIt is the color of a sunflower."
    elif (color == 'GREEN'):
        message = "Green is a nice color.\nIt is the color of the grass."
    else:
        print(f"{color} is a nice color")

    # Print message to the user
    print(message)

# Run main()
main()
