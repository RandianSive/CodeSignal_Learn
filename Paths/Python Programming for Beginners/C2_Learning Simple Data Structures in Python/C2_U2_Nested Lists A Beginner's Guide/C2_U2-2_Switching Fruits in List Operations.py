# Given a nested list 
grocery_list = [['apple', 'banana', 'cherry'], ['carrot', 'lettuce', 'broccoli'], ['rice', 'bread', 'noodles']]

# Implementing count() method
fruit_count = grocery_list[0].count('banana')

# Checking if 'banana' exists in the first sublist using 'in'
check_banana = 'banana' in grocery_list[0]

print("Number of 'banana' in the first sublist:", fruit_count)
print("Does 'banana' exist in the first sublist?", check_banana)