planets_sizes = [4879, 12104, 12756, 6792, 142984, 120536, 51118, 49528] # diameters of planets (Mercury to Neptune) in km
planets_names = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# The zip function helps us create a tuples list with planet name and its size for easier identification
planets_tuples = list(zip(planets_names, planets_sizes))
print(planets_tuples)