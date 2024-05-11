# Below is the list representing the sizes of some planets in our cosmos in thousands of kilometers.
planet_sizes = [20, 32, 12, 65, 30, 10]

# TODO: Use Python's built-in function to find the size of the smallest planet and print it
min_planet = min(planet_sizes)
print(f"Smallest planet size is: {min_planet} million meters.")

# TODO: Find the total size of all planets in the list and print it
total_planet_size = sum(planet_sizes)
print(f"Total planet size is: {total_planet_size} million meters.")

# TODO: Order the planets by their size and print the ordered list
ordered_planet_sizes = sorted(planet_sizes)
print(ordered_planet_sizes)