# Assume we have different types of fruits in two separate baskets
basket_A = {"apple", "banana", "orange", "cherry", "pear"}
basket_B = {"kiwi", "mango", "banana", "apple", "guava"}

# Find fruits that are present only in basket A, but not in basket B

fruits = basket_A - basket_B
print(fruits)