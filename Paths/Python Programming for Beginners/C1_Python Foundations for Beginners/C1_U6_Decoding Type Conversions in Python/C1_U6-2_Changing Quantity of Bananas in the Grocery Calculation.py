# The prices for the fruits are stored as strings
apple_price = "1.0"
banana_price = "0.5"
cherry_price = "0.1"

# Convert the prices from string to float
apple_price_float = float(apple_price)
banana_price_float = float(banana_price)
cherry_price_float = float(cherry_price)

# Now, calculate the total cost of buying 3 apples, 2 bananas, and 5 cherries
total_price = (apple_price_float * 3) + (banana_price_float * 4) + (cherry_price_float * 5)

# Print out the result
print("Total cost: $", int(total_price))