class Satellite:
    def __init__(self, name, mission_type):
        self.name = name
        self.mission_type = mission_type

satellite1 = Satellite("Hubble", "Space Telescope")
satellite2 = Satellite("GPS", "Navigation")

print(satellite1.name, satellite1.mission_type) # Prints: Hubble, Space Telescope
print(satellite2.name, satellite2.mission_type) # Prints: GPS, Navigation