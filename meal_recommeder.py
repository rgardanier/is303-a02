'''
Ryan Gardanier
IS 303
Meal Recommender

Inputs: 
- ask the user for the meal they want to eat (breakfast, lunch, or dinner)
- ask the user if they have dietary restrictions (vegitarian, vegan, gluten_free)
- ask the user for a budget for the meal (low, medium, high)

Processes:
- based on the user's meal choice, dietary restrictions, and budget, the program will give them a meal recommendation

Outputs:
- use an f string to format the meal recommendation

'''

# Inputs
valid_meals = ['breakfast', 'lunch', 'dinner']
while True:
    meal = input("What meal do you want to eat? (breakfast, lunch, or dinner): ").lower()
    if meal in valid_meals:
        break
    else:
        print("The meal you entered is invalid. Please enter 'breakfast', 'lunch', or 'dinner'.")

valid_dietary_restrictions = ['vegetarian', 'vegan', 'gluten free', 'none']
while True:
    dietary_restrictions = input("Do you have any dietary restrictions? (vegetarian, vegan, gluten free, or none): ").lower()
    if dietary_restrictions in valid_dietary_restrictions:
        break
    else:
        print("The dietary restriction you entered is invalid. Please enter 'vegetarian', 'vegan', or 'gluten free'.")

valid_budgets = ['low', 'medium', 'high']
while True:
    budget = input("What is your budget? (low, medium, or high}: ").lower()
    if budget in valid_budgets:
        break
    else:
        print("The budget you entered is invalid. Please enter 'low', 'medium', or 'high'. ")

# processes
if meal == "breakfast":
    if dietary_restrictions == "vegetarian":
        if budget == "low":
            recommendation = "Oatmeal with fruit"
        elif budget == "medium":
            recommendation = "Avocado toast with eggs"
        else:
            recommendation = "Vegetarian omelette with toast and fruit"
    elif dietary_restrictions == "vegan":
        if budget == "low":
            recommendation = "Smoothie bowl with fruit and granola"
        elif budget == "medium":
            recommendation = "Vegan pancakes with syrup and fruit"
        else:
            recommendation = "Vegan breakfast burrito with tofu scramble, sweet potatoes, and avocado"
    elif dietary_restrictions == "gluten free":
        if budget == "low":
            recommendation = "Yogurt with fruit and gluten free granola"
        elif budget == "medium":
            recommendation = "Gluten free toast with eggs and avocado"
        else:
            recommendation = "Gluten free breakfast sandwhich with eggs, bacon, and cheese"
elif meal == "lunch":
    if dietary_restrictions == "vegetarian":
        if budget == "low":
            recommendation = "Grilled cheese sandwhich with tomato soup"
        elif budget == "medium":
            recommendation = "Avocado salad with quinoa"
        else:
            recommendation = "Vegetarian pasta with garlic bread and salsa"
    elif dietary_restrictions == "vegan":
        if budget == "low":
            recommendation = "Vegan wrap with hummus, lettuce, and tomato"
        elif budget == "medium":
            recommendation = "Vegan burger"
        else:
            recommendation = "Vegan pizza"
    elif dietary_restrictions == "gluten free":
        if budget == "low":
            recommendation = "Gluten free sandwhich"
        elif budget == "medium":
            recommendation = "Gluten free salad"
        else:
            recommendation = "Gluten free pasta"
else: #meal == "dinner":
    if dietary_restrictions == "vegetarian":
        if budget == "low":
            recommendation = "taco soup"
        elif budget == "medium":
            recommendation = "Vegitarian stir fry"
        else:
            recommendation = "Vegetarian lasagna"
    elif dietary_restrictions == "vegan":
        if budget == "low":
            recommendation = "Vegan salad"
        elif budget == "medium":
            recommendation = "Vegan burger"
        else:
            recommendation = "Vegan pizza"
    elif dietary_restrictions == "gluten free":
        if budget == "low":
            recommendation = "Green beans with potatoes and chicken"
        elif budget == "medium":
            recommendation = "Gluten free italian chicken"
        else:
            recommendation = "Gluten free pasta"
# Outputs:
print(f"Based on your meal choice, dietary restrictionos, and budget, I recommend you eat {recommendation}.")