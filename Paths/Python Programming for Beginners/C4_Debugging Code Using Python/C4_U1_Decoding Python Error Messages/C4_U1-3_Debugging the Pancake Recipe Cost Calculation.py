# A recipe for Pancakes with cost for ingredients
# Each ingredient (string) corresponds to a tuple: amount and cost
recipe_ingredients = {"eggs": (2, 0.5), "milk": (1, 1.5), "sugar": (0.05, 0.2), "butter": (0.1, 1.2), "flour": (0.3, 0.5)}

# Calculate and print the total cost of the recipe
total_cost = 0
for ingredient, (amount, cost) in recipe_ingredients.items():
    total_cost += amount * cost

print("The total cost of the Pancakes recipe is " + str(total_cost))