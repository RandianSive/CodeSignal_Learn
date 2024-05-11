# TODO: Define a function that calculates the total price of an order
# This function should take three arguments: the price of a burger, fries, and a drink
def calculate_total(burger, fries, drink):
    return burger + fries + drink


# TODO: Specify the prices for a burger, fries, and a drink
burger_price = 10
fries_price = 5
drink_price = 4


# TODO: Call your function with the prices of the items and assign the result to a variable
order_total = calculate_total(burger_price,fries_price,drink_price)


# TODO: Print out the total cost of the order
print(f"Total cost of the order is : {order_total}")