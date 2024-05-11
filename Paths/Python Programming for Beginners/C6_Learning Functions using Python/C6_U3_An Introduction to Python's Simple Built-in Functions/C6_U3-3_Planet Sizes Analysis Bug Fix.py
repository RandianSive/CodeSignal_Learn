# List of the sizes of 5 planets in kilometers
planet_sizes = [12341, 6786, 2435, 3475, 3999]
min_size = min(planet_sizes)
max_size = max(planet_sizes)
total_sizes = sum(planet_sizes)
average_size = round(total_sizes / len(planet_sizes))

print(f"The smallest planet is {min_size} kilometers.")
print(f"The largest planet is {max_size} kilometers.")
print(f"The total size of the planets is {total_sizes} kilometers.")
print(f"The average size of the planets is {average_size} kilometers.")