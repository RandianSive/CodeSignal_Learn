user_role = "guest"
file_read_permission = False

# TODO: Determine the access type using a ternary conditional operator based on user_role and file_read_permission
accessible = True if user_role == "admin" or file_read_permission == True else False


# TODO: Print the access type
print("Access Granted" if accessible else "Access Denied")