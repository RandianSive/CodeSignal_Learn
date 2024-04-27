# The solar system in string
solar_system = "Mercury,Venus,Earth,Mars,Jupiter,Saturn,Uranus,Neptune"

# Get the planet names in a list using str.split(separator)
planets = solar_system.split(",")

# Use the string repetition operation (*) to repeat and show each planet name 3 times
for planet in planets:
    print((planet + ' ') * 3)