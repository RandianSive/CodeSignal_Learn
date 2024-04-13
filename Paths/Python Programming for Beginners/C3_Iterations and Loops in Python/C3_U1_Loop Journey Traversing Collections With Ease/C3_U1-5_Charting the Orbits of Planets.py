# List of planets
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# A dictionary of orbit periods (days) for planets
orbit_periods = {
    'Mercury': 88,
    'Venus': 225,
    'Earth': 365,
    'Mars': 687,
    'Jupiter': 4333,
    'Saturn': 10759,
    'Uranus': 30687,
    'Neptune': 60190,
}

# TODO: For each planet in the 'planets' list, print the name of the planet
# and its orbit period in Earth days, from the 'orbit_periods' dictionary.

for planet in planets:
    print(f"{planet} has an orbit period of {orbit_periods[planet]} Earth days.")