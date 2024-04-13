# Let's allow only those party guests who bring at least 10 fruits.
guests = [('Alice', 15), ('Bob', 5), ('Charlie', 8), ('Daisy', 20), ('Eve', 0), ('Frank', 18)]

for guest in guests:
    # TODO: add an if-else condition to control guest entry based on the number of star fruits they bring.
    if guest[1] >=10:
        print(f"Welcome to the party, {guest[0]}!")
    # If they brought less than 10 fruits, they are not allowed in.
    elif guest[1] <10:
        print(f"You are not allowed to enter the party, {guest[0]}!")