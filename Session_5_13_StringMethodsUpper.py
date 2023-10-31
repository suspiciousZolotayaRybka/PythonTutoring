def main():
    color = input("Please enter your favorite color (blue/yellow/green):")

    # Set color to all lowercase
    color = color.lower()
    
    # Assign message based on the users favorite color
    if (color == 'blue'):
        print("Blue is a nice color.\nIt is the color of the ocean.")
    elif (color == 'yellow'):
        print("Yellow is a nice color.\nIt is the color of a sunflower.")
    elif (color == 'green'):
        print("Green is a nice color.\nIt is the color of the grass.")
    else:
        print(f"{color.capitalize()} is a nice color.")
        
main()
