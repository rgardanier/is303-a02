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
can_continue = True
color1 = input("Enter the first primary color you want to mix (blue, red, yellow): ").lower()
if color1 not in ["blue", "red", "yellow"]:
    print("I didn't recognize that color. Please make sure you entered a valid primary color (blue, red, yellow).")
    can_continue = False
color2 = input("Enter the second primary color you want to mix (blue, red, yellow): ").lower()
if color2 not in ["blue", "red", "yellow"]:
    print("I didn't recognize that color. Please make sure you entered a valid primary color (blue, red, yellow).")
    can_continue = False

# processes
if color1 == "blue" and can_continue == True:
    if color2 == "red":
        result = "purple"
    elif color2 == "yellow":
        result = "green"
    else:
        result = "blue"
else:
    print("This program doesn't work because you entered an invalid color. Please run the program again and make sure to enter a valid primary color.")

if color1 == "red" and can_continue == True:
    if color2 == "blue":
        result = "purple"
    elif color2 == "yellow":
        result = "orange"
    else:
        result = "red"
else:
    print("This program doesn't work because you entered an invalid color. Please run the program again and make sure to enter a valid primary color.")

if color1 == "yellow" and can_continue == True:
    if color2 == "blue":
        result = "green"
    elif color2 == "red":
        result = "orange"
    else:
        result = "yellow"
else:
    print("This program doesn't work because you entered an invalid color. Please run the program again and make sure to enter a valid primary color.")

# outputs
if can_continue == True:
    print(f"When you mix {color1} and {color2}, you get {result}.")

    

    
