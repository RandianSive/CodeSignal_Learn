# We have our fruit baskets ready, let's look for new fruits!
basket_X = {"banana", "kiwi", "apple", "orange"}
basket_Y = {"banana", "cherry", "kiwi", "mango"}

# TODO: Use set operations to find the total number of unique fruits in both baskets
unique_fruit = sorted(basket_X | basket_Y)

# TODO: Find the fruit that comes first in alphabetical order and print it
print(unique_fruit[0])