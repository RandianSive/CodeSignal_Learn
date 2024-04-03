grocery_list = [['apple', 'banana', 'cherry'], ['carrot', 'lettuce', 'broccoli'], ['rice', 'bread', 'noodles']]

# Updating 'banana' to 'kiwi' in the first sublist
grocery_list[0][1] = 'kiwi'

# Deleting 'lettuce' from the second sublist
del grocery_list[1][1]

# Adding 'potato' to the second sublist
grocery_list[1].append('potato')

# Inserting a new sublist of cleaning products
grocery_list.insert(3, ['soap', 'shampoo', 'toothpaste'])

print(grocery_list)