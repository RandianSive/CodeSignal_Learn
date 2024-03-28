# Variables for bank transactions
account_balance = 1000   # account_balance is the current balance in the account
deposit_amount = 600     # deposit_amount is how much you want to deposit

# Perform arithmetic operation for depositing amount into account_balance
new_balance = account_balance + deposit_amount
print('Your new balance is:', new_balance)  # Print the new balance after deposit

# Verify if the new balance is more than or equal to a VIP status threshold of 1500 using the logical operator
vip_status = new_balance > 1500
print('VIP Status:', vip_status)  