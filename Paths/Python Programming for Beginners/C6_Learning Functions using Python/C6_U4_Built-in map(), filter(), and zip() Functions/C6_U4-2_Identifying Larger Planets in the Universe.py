# Let's continue our space exploration and further explore the secrets of the Universe!

planet_sizes = [100, 125, 90, 95, 110, 120, 155]  # Planet sizes in arbitrary units
planet_names = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Neptune']  # Names of respective planets

def filter_size(size):
    return size > 100

# The filter() function filters out items based on a condition. Here, we are using it to filter planets that are greater than 100.
big_planets = list(filter(filter_size, planet_sizes))

# The zip() function pairs elements from two lists. Here, we are using it to pair planet names with their relative sizes.
planet_size_pairs = list(zip(planet_names, planet_sizes))

print("Sizes of planets: ", planet_sizes)
print("Planets greater than 100: ", big_planets)

greater_planet_list = []

for planet in planet_size_pairs:
    if filter_size(planet[1]):
        greater_planet_list.append(planet)

print("Planet names and their respective sizes: ", greater_planet_list)