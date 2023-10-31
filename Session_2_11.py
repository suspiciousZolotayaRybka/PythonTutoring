# Prompt user for weather and temperature information
is_sunny = eval(input("Is it sunny?\nEnter True or False\n=>"))
temperature = float(input("What is the temperature?\n=>"))

# Assign a recommended_activity to the user based on weather and temperature status
if (temperature >= 70 and is_sunny):
    recommended_activity = "Let's go to the pool!"
    
elif (temperature < 70 and is_sunny):
    recommended_activity = "Let's go hiking!"
    
elif (temperature >= 70 and not(is_sunny)):
    recommended_activity = "Let's go to an indoor museum!"
    
else:
    # temperature is less than 70 and it is not sunny
    recommended_activity = "Let's have a movie day at home!"

# Output the weather information and activity recommendation using the format function
print("The current temperature is: {:.2f}".format(temperature))
print(f"It is currently sunny: {is_sunny}")
print(recommended_activity)
