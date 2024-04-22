# Imagine we have 3 planets in a cosmos that have different numbers of satellites.
satellites = {'Earth': 1, 'Mars': 2, 'Neptune': 14}

# TODO: For each planet, print its name along with the number of satellites it has.
for planet,satellite in satellites.items():
    print(f"{planet} has {satellite} satellite(s).")
# TODO: For each satellite of a planet, print its order around that planet.
# For example: Satellite 1 around Earth
# For example: Satellite 12 around Neptune
for planet,satellite in satellites.items():
    count = 1
    while count <= satellite:
        print(f"Satellite {count} around {planet}")
        count +=1