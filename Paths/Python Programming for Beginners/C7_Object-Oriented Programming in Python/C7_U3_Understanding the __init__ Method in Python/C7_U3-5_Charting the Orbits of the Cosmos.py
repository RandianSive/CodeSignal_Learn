# TODO: Define a class named "Planet" with a constructor
#       The constructor should accept two attributes: "name" and "orbit"
class Planet:
    def __init__(self, name, orbit):
        self.name = name
        self.orbit = orbit
    

# TODO: Create two Planet instances, name them "Earth" and "Mars"
#       Both objects orbit the "Sun"

earth = Planet("Earth", "Sun")
mars = Planet("Mars","Sun")

# TODO: For each Planet instance, print its name and what it orbits around
print(f"{earth.name} orbits the {earth.orbit}.")
print(f"{mars.name} orbits the {mars.orbit}.")