# A string representing solar system planets
planets = "Earth Mars Venus Jupiter Saturn Uranus Neptune Pluto"

# Split the string into a list of planet names
planet_list = planets.split(' ')

# TODO: Join the planet list into a string with '|' as a separator and assign it to the variable 'solar_system'

solar_system = "|".join(planet_list)

print(solar_system)