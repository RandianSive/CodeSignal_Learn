guests = [('Obi-Wan', 'VIP'), ('Anakin', 'Regular'), ('Yoda', 'VIP'), ('Jar Jar', 'Unwanted'), ('Leia', 'Regular'), ('Han', 'VIP')]
for guest in guests:
   if guest[1] == 'VIP':
      print("Welcome, Master", guest[0], ", we've been expecting you!")
   else:
      print(f"Sorry, {guest[0]}, this is not the party you're looking for.")