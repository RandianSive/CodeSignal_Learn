stars = ["Alpha Centauri", "Betelgeuse", "Capella"]
planets = ["Earth", "Mars", "Venus"]


for star in stars:
    print(f"{star} sees:", end=" ")
    print(", ".join(planets))