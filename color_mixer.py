'''
Ryan Gardanier
IS 303
Color Mixer

Inputs:
- ask user for two primary colors
- checks if the input that was given is valid
- if not, tell the user that the input was invalid and ask them to try again
Processes:
- mix the two primary colors together to create a secondary color
- blue + red = purple
- blue + yellow = green
- red + yellow = orange
- if the user enters the same color twice, the output will be that color
Outputs:
- output the secondary color that was created by mixing the two primary colors together
'''

# inputs
valid_colors = ['blue', 'red', 'yellow']
while True:
    color1 = input("Please enter the first primary color (blue, red, or yellow: ").lower()
    if color1 in valid_colors:
        break
    else:
        print("The color you entered is invalid. Please enter 'blue', 'red', or 'yellow'.")

while True:
    color2 = input("Please enter the second primary color (blue, red, or yellow): ").lower()
    if color2 in valid_colors:
        break
    else:
        print("The color you entered is invalid. Please enter 'blue', 'red', or 'yellow'.")

# processes
if color1 == "blue":
    if color2 == "red":
        result = "purple"
    elif color2 == "yellow":
        result = "green"
    else:
        result = "blue"
if color1 == "red":
    if color2 == "blue":
        result = "purple"
    elif color2 == "yellow":
        result = "orange"
    else:
        result = "red"
if color1 == "yellow":
    if color2 == "blue":
        result = "green"
    elif color2 == "red":
        result = "orange"
    else:
        result = "yellow"
        
# outputs
print(f"When you mix {color1} and {color2}, you get {result}.")

    

    
