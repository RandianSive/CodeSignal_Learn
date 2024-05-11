# Let's create a list of 5 planets and their distances from the Sun in millions of kilometers
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter"]
distances = [58, 108, 150, 228, 778]

# TODO: Convert these distances from kilometers to miles using `map()`
# 1 kilometer = 0.621371 mile
distances_in_miles = list(map(lambda x: x * 0.621371, distances))

# TODO: Pair up the planets and their distances in miles from the Sun using `zip()` 
planets_dist_in_miles = list(zip(planets,distances_in_miles))

# TODO: Print the final list of combined planets and their mile distance from the Sun
print(planets_dist_in_miles)