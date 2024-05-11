# Given lists of planets and their distances from the sun
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
distances = [58, 108, 150, 228, 778, 1429, 2871, 4495]  # in millions of kilometers

# We are going to use the zip() function to couple each planet with its respective distance
planet_distance = list(zip(planets, distances))

print(planet_distance)