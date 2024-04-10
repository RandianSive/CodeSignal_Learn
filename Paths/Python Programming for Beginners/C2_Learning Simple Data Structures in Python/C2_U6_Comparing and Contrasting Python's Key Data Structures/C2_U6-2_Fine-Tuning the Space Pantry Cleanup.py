# Our space mission fridge items in a list with some repeated items
fridge_items = ("apple", "banana", "orange", "apple", "kiwi", "tomato", "banana", "kiwi")

# Converting the list to a set to remove duplicates
unique_fridge_items = set(fridge_items)

# Converting the set back to a list
unique_fridge_items_list = list(unique_fridge_items)

print(unique_fridge_items_list)