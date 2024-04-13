guests = ['Alice', 'Bob', 'Charlie', 'Daisy', 'Eve', 'Frank']
for guest in guests:
    if len(guest) > 4:
        print("Welcome to the party,", guest, "!")
    elif len(guest) <= 4:
        print("Hey", guest, ", welcome!")