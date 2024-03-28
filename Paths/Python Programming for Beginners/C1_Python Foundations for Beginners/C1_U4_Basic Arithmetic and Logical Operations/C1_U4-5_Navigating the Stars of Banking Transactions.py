# Variables for bank transactions
account_balance = 50   # account_balance is the current balance in your card account
purchase_amount = 25  # purchase_amount is how much you spent on your recent purchase
cashback_amount = 5   # cashback for the purchase, in percent

# TODO: Perform arithmetic operation to calculate new balance after the purchase
account_balance -= purchase_amount
# TODO: Perform arithmetic operations to calculate the cashback value and add it back to the account balance
account_balance += purchase_amount * cashback_amount * 0.01
# TODO: Print the new account balance after purchasing and returning cashback
print(f"Account balance: {account_balance}")