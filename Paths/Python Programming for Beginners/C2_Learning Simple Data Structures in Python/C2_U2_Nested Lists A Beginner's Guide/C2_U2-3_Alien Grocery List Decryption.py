# Initial grocery list
grocery_list = [
    ['apple', 'orange'], # fruits list
    ['carrot', 'onion'], # vegetables list
    ['soap', 'shampoo'], # hygiene items list
]

# Add a new category of spices to the list with 'coriander' and 'cumin'
grocery_list.append(['coriander', 'cumin'])

# Remove 'onion' from the vegetables list
grocery_list[1].remove('onion')

# Add 'banana' to the fruit list
grocery_list[0].append('banana')

print(grocery_list)