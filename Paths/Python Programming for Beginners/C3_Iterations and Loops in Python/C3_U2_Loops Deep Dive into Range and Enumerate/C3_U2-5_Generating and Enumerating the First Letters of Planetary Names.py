planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
first_letters = [] 

# TODO: Write a for loop with a range to iterate through each planet in the planets list.
# Inside the loop, add the first letter of each planet to the first_letters list.
for planet in planets:
    first_letters.append(planet[0])

# TODO: Write a for loop using enumerate to print out each first letter and its corresponding planet index.
for index,first_letter_planet in enumerate(first_letters):
    print(f"Planet {index+1}'s first letter is {first_letter_planet}")
