# Original contact list
contact_list = ["Tom", "Jerry", "Spike", "Tyke"]

# Let's add the contact "Marvin", print the last contact now
contact_list.append("Marvin")
print(contact_list[-1])   # Outputs: 'Marvin'

# Now, let's remove the first contact from the list
# and print the second contact from the old list (Jerry)
del contact_list[0]
print(contact_list[0])    # Outputs: 'Jerry'