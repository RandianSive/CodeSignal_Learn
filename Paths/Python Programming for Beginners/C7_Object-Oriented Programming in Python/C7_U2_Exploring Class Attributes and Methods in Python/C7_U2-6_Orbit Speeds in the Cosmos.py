class Planet:
    orbit_speed = 30000  # in km/s

    def revolve(self):
        return f"Revolution speed: {self.orbit_speed} km/s"

class Cosmos:
    planet = Planet() # Construct a planet

    def orbit_speed(self):
        # TODO: find out how fast the planet is orbiting
        return self.planet.revolve()

cosmos = Cosmos()
print(cosmos.orbit_speed())  # prints speeds of planets in the cosmos