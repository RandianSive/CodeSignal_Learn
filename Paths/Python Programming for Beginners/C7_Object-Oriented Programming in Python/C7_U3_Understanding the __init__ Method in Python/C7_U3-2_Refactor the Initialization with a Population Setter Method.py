class Planet:
    def __init__(self, name):
        self.name = name
        self.population = 'Unknown'

    def set_population(self, population):
        self.population = population

earth = Planet("Earth") 
mars = Planet("Mars") 

earth.set_population(7800000000)
mars.set_population(0)

print(f"{earth.name} has a population of {earth.population} humans.")
print(f"{mars.name} has a population of {mars.population} humans.")