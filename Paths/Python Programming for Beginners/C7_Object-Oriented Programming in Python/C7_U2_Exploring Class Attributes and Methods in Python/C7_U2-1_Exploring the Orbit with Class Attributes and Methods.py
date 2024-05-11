class Planet:
    shape = "round"
    orbital_speed = 29800

    def orbit(self):
        return f"The {self.shape} planet orbits at the speed of {self.orbital_speed} km/s"

earth = Planet()
print(earth.orbit())  # prints: The round planet orbits at the speed of 29800 km/s