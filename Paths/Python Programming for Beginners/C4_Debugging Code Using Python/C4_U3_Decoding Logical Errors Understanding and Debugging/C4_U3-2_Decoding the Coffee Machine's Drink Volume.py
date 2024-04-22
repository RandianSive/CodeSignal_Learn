# Available drinks and their volumes
latte_volume = 16
cappuccino_volume = 12

# Drink choice and quantity
drink_choice = "latte"
number_of_drinks = 5

# Logical error here! Incorrect drink volume used to calculate total volume
if drink_choice == "latte":
    total_volume = latte_volume * number_of_drinks
else:
    total_volume = cappuccino_volume * number_of_drinks

print("Total volume of " + drink_choice + "s ordered: " + str(total_volume) + " oz")