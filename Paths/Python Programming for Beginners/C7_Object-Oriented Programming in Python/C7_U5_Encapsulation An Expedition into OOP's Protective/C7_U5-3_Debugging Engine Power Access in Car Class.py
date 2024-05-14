class Car:
    def __init__(self):
        self.__engine_power = 1000  # Horsepower
    
    # Getter
    def get_engine_power(self):
        return self.__engine_power
    
    # Setter
    def set_engine_power(self, power):
        self.__engine_power = power

# Instance
bently = Car()
print(bently.get_engine_power()) # Output: 1000

# Change Engine Power
bently.set_engine_power(1800)
print(bently.get_engine_power()) # Output: 1800