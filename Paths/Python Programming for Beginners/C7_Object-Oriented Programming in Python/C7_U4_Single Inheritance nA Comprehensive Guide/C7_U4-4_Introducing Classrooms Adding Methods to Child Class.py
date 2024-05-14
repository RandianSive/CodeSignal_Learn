class School:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(self.name + " is a school.")

class Classroom(School):
    def __init__(self, name, room_number):
        super().__init__(name)
        self.room_number = room_number

    # TODO: Add missing method to introduce each classroom
    def introduce(self):
        print(f"This is classroom {self.room_number} at {self.name}.")

new_school = School("Central High")
new_classroom = Classroom("Central High", "101")

new_school.introduce()  # Prints: "Central High is a school."
new_classroom.introduce()