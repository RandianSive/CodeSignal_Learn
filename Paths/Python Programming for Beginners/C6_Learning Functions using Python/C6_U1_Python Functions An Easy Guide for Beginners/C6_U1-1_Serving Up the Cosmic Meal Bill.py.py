# Defining the function to calculate the total price
def calculate_total_price(burger, drink, dessert):
    total_price = burger + drink + dessert
    return total_price

# Calling the function with prices of items
final_bill = calculate_total_price(5, 3, 4)
print("The total bill is $" + str(final_bill))