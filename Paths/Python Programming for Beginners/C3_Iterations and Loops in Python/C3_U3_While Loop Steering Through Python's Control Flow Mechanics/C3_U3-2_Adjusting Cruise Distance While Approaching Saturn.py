planet = "Saturn"
distance_from_saturn = 1433.5  # in millions of kilometers
while distance_from_saturn > 500:
    print("Navigating towards", planet, "which is", distance_from_saturn, "million km away")
    distance_from_saturn -= 100.0
print("Hello:", planet)