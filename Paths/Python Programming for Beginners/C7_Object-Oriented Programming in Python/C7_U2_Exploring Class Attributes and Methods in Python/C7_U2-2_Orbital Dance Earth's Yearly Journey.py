class Planet:
    ORBITAL_PERIOD_DAYS = 365  # Earth's orbital period in days, as a constant

    def orbit(self):
        return f"This planet orbits the Sun every {self.ORBITAL_PERIOD_DAYS} days."

earth = Planet()
print(earth.orbit())