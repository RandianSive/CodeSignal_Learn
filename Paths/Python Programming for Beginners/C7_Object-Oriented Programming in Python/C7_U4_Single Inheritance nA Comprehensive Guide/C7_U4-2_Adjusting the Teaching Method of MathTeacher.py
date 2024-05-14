class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def teach(self):
        print(self.name + " is teaching " + self.subject + ".")

class MathTeacher(Teacher):
    def teach(self):
        print(f"{self.name} is explaining complex {self.subject} problems.")

math_teacher = MathTeacher("Mrs. Smith", "math")
math_teacher.teach() # Outputs: Mrs. Smith is explaining complex math problems.