# Imagine we have 3 astronauts ready for the mission to 3 different planets
astronauts = ['Buzz', 'Neil', 'Michael']
planets = ['Mars', 'Venus', 'Jupiter']

# Let's use nested loops to assign each astronaut to each planet
for astronaut in astronauts:
    # TODO: Write a nested for loop and print statement to assign each astronaut to each planet
    for planet in planets:
        print(astronaut, "is heading to", planet)