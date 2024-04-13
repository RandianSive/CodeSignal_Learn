space_objects = ['Sun', 'Earth', 'Moon', 'Mars', 'Jupiter']

# Enumerate the space_objects list and print each object with its index
for index, space_object in enumerate(space_objects):
    print('The object at index', index, 'is', space_object)

print()

# Use the range function to iterate over space_objects in reverse order
# Start from the last element, and make the negative step to get to the previous element
for i in range(len(space_objects) - 1, -1, -1):
    print('The object at index', i, 'is', space_objects[i])