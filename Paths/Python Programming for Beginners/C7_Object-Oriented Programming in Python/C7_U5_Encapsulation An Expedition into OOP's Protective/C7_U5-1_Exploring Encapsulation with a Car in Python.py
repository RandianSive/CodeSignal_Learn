class Car:
    def __init__(self):
        self.__model = 'Sedan'
    
    # Getter for car model
    def get_car_model(self):
        return self.__model
    
    # Setter for car model
    def set_car_model(self, new_model):
        if new_model in ['Sedan', 'SUV', 'Coupe']:
            self.__model = new_model
        else:
            print("Error: Invalid car model")

# Instance
my_car = Car()
print(my_car.get_car_model()) # Output: Sedan

# Change Car Model
my_car.set_car_model('Coupe')
print(my_car.get_car_model()) # Output: Coupe