class Planet:
    def __init__(self, name, population, has_life): # TODO: your task is to initialize the planet's attributes.
        self.name = name
        self.population = population
        self.has_life = has_life

# creating an instance of the class Planet
earth = Planet("Earth", 7900000000, True)

# printing out the earth's details
print(earth.name)      
print(earth.population) 
print(earth.has_life)   