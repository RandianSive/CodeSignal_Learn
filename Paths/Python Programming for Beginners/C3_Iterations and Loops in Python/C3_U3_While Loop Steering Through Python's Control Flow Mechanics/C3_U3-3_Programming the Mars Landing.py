# Space Exploration
planet = "Mars"
distance = 0
landed = False

while not landed:
    print("Currently traveling to", planet, "and covered", distance, "million km")
    distance += 10
    if distance >= 85:
        print("Landed on", planet, "after covering", distance, "million km!")
        landed = True