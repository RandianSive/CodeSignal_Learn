# Variables describing a product and its quantity in the cart
item_price = 30

# Variables describing the shopper's budget and current balance
shopper_budget = 20
shopper_balance = 50

# TODO: Add the line of code to check if the shopper has enough balance to buy a single item
print(f"Shopper's balance can buy single item: {shopper_balance >= item_price}")
# TODO: Add the line of code to check if the shopper needs to adjust their budget (whether a single item fits their budget)
print(f"Shopper's budget can buy single item: {shopper_budget >= item_price}")