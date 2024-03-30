role = "guest"
file_permission = "write"

if role == "admin":
    if file_permission == "write":
        print("File write operation granted.")
    else:
        print("File write operation denied.")
else:
    print("Access denied. Only admins can perform file write operations.")