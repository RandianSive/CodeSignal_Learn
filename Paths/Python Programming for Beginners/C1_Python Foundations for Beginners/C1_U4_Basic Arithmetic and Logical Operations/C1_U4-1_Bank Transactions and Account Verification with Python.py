# Variables for bank transactions
account_balance = 500   # account_balance is the current balance in the account
withdraw_amount = 300   # withdraw_amount is how much you want to withdraw

# Perform arithmetic operation for withdrawing amount from account_balance
new_balance = account_balance - withdraw_amount
print('Your new balance is:', new_balance)  # Print the new balance after withdrawal

# Verify if the new balance is less than a minimum balance of 200 using the logical operator
account_status = new_balance >= 200
print('Account Active Status:', account_status)  