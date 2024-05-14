# TODO: Define an Automobile class with a private attribute assigned in the constructor
    # TODO: Create a getter method for the private attribute
    # TODO: Create a setter method for the private attribute
class Automobile:
    def __init__(self):
        self.__brand = "Unknown"
        
    def get_brand(self):
        return self.__brand
        
    def set_brand(self,brand):
        self.__brand = brand
        
# TODO: Instantiate the class
# TODO: Use the getter to print the value of the private attribute
# TODO: Use the setter to change the value of the private attribute
# TODO: Use the getter again to print the new value of the private attribute

honda = Automobile()

print(honda.get_brand())

honda.set_brand("Honda")
print(honda.get_brand())