class Spaceship:
    def __init__(self):
        self.__fuel_type = 'Nuclear'

    # Getter
    # TODO: Add a method to retrieve the fuel type of the spaceship
    def get_fuel_type(self):
        return self.__fuel_type

    # Setter
    # TODO: Add a method to set a different fuel type for the spaceship
    def set_fuel_type(self,fuel_type):
        self.__fuel_type = fuel_type

# Instance
enterprise = Spaceship()
print(enterprise.get_fuel_type()) # Output: Nuclear

# Change Fuel Type
enterprise.set_fuel_type('Antimatter')
print(enterprise.get_fuel_type()) # Output: Antimatter