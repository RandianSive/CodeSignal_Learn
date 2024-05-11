# TODO: Create a class named Planet, assign the name of the planet and its gravity constant

"""
    TODO: Add a method inside the class that takes object_mass as a parameter
    and calculates the force exerted on an object.
    Formula: force = gravity_constant * object_mass
    
    The method should return a string representing a nice message
    including the object's name and the force.
"""

class Planet:
    def __init__(self, name, gravity_constant=9.81):
        self.name = name
        self.GRAVITY_CONSTANT = gravity_constant

    def calculate_force(self, input_mass):
        return f"Force of {self.name} is {self.GRAVITY_CONSTANT*input_mass:.2f}N."
    

# TODO: Create an object named `earth` of class `Planet`

earth = Planet("Earth")

# TODO: Calculate and print the force exerted by earth on an object of mass 10kg

print(earth.calculate_force(10))