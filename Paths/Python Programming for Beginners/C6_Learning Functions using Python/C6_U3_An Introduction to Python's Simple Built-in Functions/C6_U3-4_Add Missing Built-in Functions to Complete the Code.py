# A list of the distances of planets from the Sun in astronomical units (AU)
planet_dist = [0.39, 0.723, 1, 1.524, 5.203, 9.537, 19.18, 30.07, 39.48] 

print("Total number of planets: ", len(planet_dist)) 
print("Closest planet to the Sun: ", min(planet_dist), "AU") 
# TODO: Write the command to find and print the max value from the list
max_dist = max(planet_dist)
print(f"Farthest planet from the Sun: {max_dist} AU.")
# TODO: Write the command to sum up the elements of the list, then print the sum
total_dist = sum(planet_dist)
print(f"Total planet distance to the Sun: {total_dist} AU.")