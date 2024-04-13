# You are hosting a party, and you have guests in line. 
# You will invite-only VIPs and Regular guests until the time is up!
# Your goal is to greet as many people as you can, or else the party might be too quiet.

guests = [('Alice', 'VIP'), ('Bob', 'VIP'), ('Charlie', 'Regular'), ('Daisy', 'Unwanted'), ('Eve', 'VIP'), ('Frank', 'Regular'), ('Marcelo', 'VIP')]
time_left = 5

for guest in guests:
  if time_left == 0:
      break
  if guest[1] != 'Unwanted':
      print("Welcome,", guest[0], "!")
      time_left -= 1
  else:
      print("Sorry,", guest[0], ", we cannot invite you this time!")