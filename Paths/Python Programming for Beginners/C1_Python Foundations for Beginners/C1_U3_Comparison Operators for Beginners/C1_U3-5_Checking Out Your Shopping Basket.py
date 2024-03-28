# Shopping scenario
fruit = "banana"
favorite_fruit = "apple"

# TODO: Compare the fruit names and assign result to variable 'match', using comparison operators. 
# TODO: Print the result. Your print statement should read, "Is the supermarket's fruit the same as the favorite fruit?"
match = fruit == favorite_fruit
print(f"Is the supermarket's fruit the same as the favorite fruit? {match}")


# Comparing prices
price_banana = 3  # price for banana is $3
money_in_wallet = 5  # You only have $5 in your wallet

# TODO: Use the comparison operator to check if you have enough money to buy the banana and assign the result in the variable 'can_buy'.
# TODO: Print the result. Your print statement should read, "Do you have enough money to buy the banana?"
can_buy = money_in_wallet >= price_banana
print(f"Do you have enough money to buy the banana? {can_buy}")