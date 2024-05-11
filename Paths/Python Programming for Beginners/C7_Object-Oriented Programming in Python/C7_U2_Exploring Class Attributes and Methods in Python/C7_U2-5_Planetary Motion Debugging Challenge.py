class Planet:
    orbit_speed = 29.78  # kilometers per second

    def rotate(self):
        return f"Planet rotates at {self.orbit_speed}km/s around the sun."

earth = Planet()
print(earth.rotate())