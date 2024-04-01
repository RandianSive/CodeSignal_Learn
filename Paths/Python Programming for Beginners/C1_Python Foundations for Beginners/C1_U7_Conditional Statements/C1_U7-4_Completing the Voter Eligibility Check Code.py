user_age = 14
voter_id_available = True

if user_age >= 21 and voter_id_available == True:
    user_eligible_message = "You are eligible to vote!"
elif user_age < 21 or voter_id_available != True:
    user_eligible_message = "You need to be at least 21 years old and have a voter ID to vote!"

print(user_eligible_message)