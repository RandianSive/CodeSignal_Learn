# Variables for bank transactions
account_balance = 1200    # account_balance holds the current balance in the account
loan_amount = 1500        # loan_amount is the amount you want to borrow from the bank
interest_rate = 0.05      # interest_rate is the interest charged by the bank

# Perform arithmetic operation for adding the loan amount to account_balance 
account_balance += loan_amount
print("Your account balance after the loan deposit:", account_balance)  

# TODO: Calculate the interest for the loan - it is a multiplication of the loan amount and interest rate
loan_interest = loan_amount * interest_rate
# TODO: deduct the interest from the account balance and print the updated account balance.
account_balance -= loan_interest
print(f"Your account balance after the loan interest withdraw: {account_balance}")