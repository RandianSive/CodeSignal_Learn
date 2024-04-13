planet = "Earth"
distance = 10 # distance, in millions of km

# TODO: Write a while loop that:
# Prints the current distance to Earth
# Decreases the distance between the Earth and the spacecraft by 1 million km until it reaches Earth.
while distance > 0:
    print("Spacecraft is", distance, "million km away from", planet)
    distance -= 1
print("We reached Earth!")