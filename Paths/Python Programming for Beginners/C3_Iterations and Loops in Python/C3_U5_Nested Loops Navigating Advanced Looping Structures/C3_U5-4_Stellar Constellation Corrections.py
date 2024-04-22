# Initializing the stars and constellations
stars_in_sky = ['Alpha', 'Beta', 'Gamma', 'Delta']
constellations = ['Orion', 'Cancer', 'Gemini']

# Nested loop representation of stars and their constellations
for constellation in constellations:
    for star_in_sky in stars_in_sky:
        print("Does star", star_in_sky, "belong to the", constellation, "constellation?")