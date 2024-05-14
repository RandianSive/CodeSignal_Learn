class Car:
    def __init__(self):
        self.__registration_number = 'UNKNOWN' # Private variable

    # Getter
    def get_registration_number(self):
        return self.__registration_number

    # Setter
    def set_registration_number(self, plate_number):
        self.__registration_number = plate_number

# Create a car with a license plate
toyota = Car()
toyota.set_registration_number('123-XYZ')
print(toyota.get_registration_number())  # Output: 123-XYZ