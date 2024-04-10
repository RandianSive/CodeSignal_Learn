# This is our assigned space mission shopping list
shopping_list = ["Spacesuit", "Space food", "Spacesuit", "Oxygen tank", "Rocket fuel", "Oxygen tank"]

# We convert this list into a set to eliminate duplicates
shopping_set = set(shopping_list)

# We then convert it back into a list for ease of access
revised_shopping_list = list(shopping_set)
print("Revised mission shopping list: ", revised_shopping_list)