# List of planet names
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

# List of planet sizes in square kilometers
sizes = [47420000, 46023860, 510072000, 144798500, 61419434000, 42710862000, 8082923000, 7615924000]

# TODO: Utilize the zip function to combine the planet names and sizes
planets_sizes = list(zip(planets,sizes))

def size_filter(planet_tuple):
    # TODO: implement a filter function that returns whether a `planet_tuple` (planet, size)
    # has a size of at least 500 million
    return planet_tuple[1] >= 500000000

greater_planets_sizes = []

# TODO: Utilize the filter function to filter only tuples (planet, size) with a size of at least 500000000
for planet_size in planets_sizes:
    if size_filter(planet_size):
        greater_planets_sizes.append(planet_size)
        

# TODO: print the filtered combination of planets and their sizes
print(greater_planets_sizes)