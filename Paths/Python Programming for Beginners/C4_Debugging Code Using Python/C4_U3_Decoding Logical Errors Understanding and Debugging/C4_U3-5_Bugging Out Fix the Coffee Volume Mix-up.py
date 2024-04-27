latte_volume = 16
cappuccino_volume = 12

# Initial order
order_latte = 3
order_cappuccino = 2

# Logical error here! Incorrect volumes used to calculate total coffee volume
total_coffee_volume = (cappuccino_volume * order_cappuccino) + (latte_volume * order_latte)
print("Total coffee volume is", total_coffee_volume)