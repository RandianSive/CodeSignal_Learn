class School:
    def __init__(self, name):
        print("Calling the School constructor")
        self.name = name

class Teacher(School):
    def teach(self):
        print(self.name + " is teaching at school.")

teacher = Teacher("Mrs. Smith") # also calls the School constructor
teacher.teach() # Prints: "Mrs. Smith is teaching at school."