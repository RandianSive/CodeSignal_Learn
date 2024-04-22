stars_data = ["Kepler-22b", "Proxima Centauri b", "Trappist-1d", "Tres-2b", "Black Hole", "Wasp-12b"]

for star in stars_data:
    if star == "Black Hole":
        print("Black hole detected! Terminating observation for safety.")
        break
    print(f"Now observing: {star}")