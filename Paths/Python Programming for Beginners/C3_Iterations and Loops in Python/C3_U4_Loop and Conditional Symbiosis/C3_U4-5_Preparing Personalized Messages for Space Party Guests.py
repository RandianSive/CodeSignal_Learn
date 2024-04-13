# You are hosting a party, and you have a list of guests.
# Some guests confirmed their attendance with "Yes", some didn't reply with "No Reply", and some declined your invite with "No".
# As part of the preparation, let's go through the list of guests and check who's coming for the party!

guest_list = [('Alice', 'Yes'), ('Bob', 'No Reply'), ('Charlie', 'No'), ('Daisy', 'Yes'), ('Eve', 'No Reply'), ('Frank', 'No')]

# TODO: Loop through the guest list
for guest in guest_list:
    # TODO: If the guest confirmed their attendance, print a welcome message.
    if guest[1] == "Yes":
        print(f"Welcome to the party, {guest[0]}!")
    # TODO: If the guest didn't reply, print a message of uncertain attendance.
    elif guest[1] == "No Reply":
        print(f"Not sure whether {guest[0]} will come to the party.")
    # TODO: If the guest declined the invite, print a message of unavailability.
    elif guest[1] == "No":
        print(f"{guest[0]} will not attend the party.")