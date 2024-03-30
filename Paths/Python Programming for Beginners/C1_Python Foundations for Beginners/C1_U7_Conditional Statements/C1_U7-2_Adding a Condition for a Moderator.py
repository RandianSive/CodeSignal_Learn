user = "moderator"

if user == "admin":
    print("You have full access.")
elif user == "moderator":
    print("You have moderator privileges!")
elif user == "member":
    print("You have member privileges.")
else:
    print("Access limited.")