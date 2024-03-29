# Grocery shopping scenario - Let's convert fruit prices and do some simple calculations
apple_price = "1.5"
banana_price = "2.0"

# Convert those fruit prices from string to float
apple_price_float = float(apple_price)
banana_price_float = float(banana_price)

total = (apple_price_float * 3) + (banana_price_float * 2)

# Print out the result
# TODO: Print the result with the format: "Total cost for 3 apples and 2 bananas: $ <total>" 

print(f"Total cost for 3 apples and 2 bananas: ${total}")