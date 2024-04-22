# Cosmos, planets, and orbits.
cosmos = 1  # The cosmos

while cosmos <= 3:  # For each cosmos 
    print("Cosmos: ", cosmos)
    planet = 1  # Each cosmos has planets
    while planet <= 3:  # For each planet in the cosmos
        print("Planet: ", planet)
        # TODO: Implement an innermost loop for the orbits of each planet.
        # Assume that each planet has 3 orbits
        # For each orbit, print it.
        orbit = 1
        while orbit <=3:
            print("Orbit: ",orbit)
            orbit += 1
        planet += 1  # Move to the next planet
    cosmos += 1  # Move to the next cosmos