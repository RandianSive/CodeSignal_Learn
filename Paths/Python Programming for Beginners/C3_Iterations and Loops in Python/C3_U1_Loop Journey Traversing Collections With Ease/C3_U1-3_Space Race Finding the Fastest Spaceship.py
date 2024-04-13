# List of spaceship speeds in km/s
speeds = {28, 50, 120, 75, 98}

# Initialize variable
fastest_speed = 0

# TODO: Write a loop to go through each speed in the list.
# If the speed element from the list is faster than the current 'fastest_speed', update 'fastest_speed' to this new speed.
for speed in speeds:
    if speed > fastest_speed:
        fastest_speed = speed

# Print the fastest speed
print("The fastest spaceship speed is", fastest_speed, "km/s.")