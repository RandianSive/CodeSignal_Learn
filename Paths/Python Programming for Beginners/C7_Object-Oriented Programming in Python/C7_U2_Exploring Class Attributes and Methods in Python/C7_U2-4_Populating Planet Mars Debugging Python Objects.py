class Planet:
    name = "Mars"
    gravity = 3.721 # measured in m/s^2
    population = 0 

    def populate(self, num):
        self.population += num
        return f"The population of {self.name} is now {self.population}."

mars = Planet()
print(mars.populate(100))  # prints: The population of Mars is now 100.