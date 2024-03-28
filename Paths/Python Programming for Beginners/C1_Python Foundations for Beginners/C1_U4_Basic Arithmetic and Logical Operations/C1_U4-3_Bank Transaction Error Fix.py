# Variables for bank transactions
account_balance = 1000   # account_balance is the current balance in the account
service_charge = 50      # service_charge is the bank's monthly service charge

# Perform arithmetic operation for subtracting service charge from account_balance
new_balance = account_balance - service_charge
print('Your new balance is:', new_balance)  # Print the new balance after the service charge

# Verify if the new balance is greater than 0 using the logical operator
account_status = new_balance > 0
print('Account Active Status:', account_status)   # Print the account status