# Function to calculate the total amount
def calculate_total(*spendings):
    # TODO: Calculate and return the total amount of spending
    return sum(spendings)

# Order made: 1 pizza, 2 burgers, and 3 soft drinks
# Their prices are 10.5, 6.75, and 2.5 respectively
total_amount = calculate_total(10.5, 6.75, 6.75, 2.5, 2.5, 2.5)

print("Your total bill is: $", total_amount)