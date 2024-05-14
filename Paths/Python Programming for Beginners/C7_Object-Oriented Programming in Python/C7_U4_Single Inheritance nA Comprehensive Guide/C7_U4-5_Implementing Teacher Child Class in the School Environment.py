# TODO: Define a class "SchoolMember" with an initialization method that accepts two arguments: "name" and "age". 
# This method should assign these arguments to respective instance variables.
# Attach a method 'introduce()' that prints the name and age of the instance in a sentence.

class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"This is {self.name}, age {self.age}.")

# TODO: Define a child class "Teacher" that inherits from the "SchoolMember" class. 
# The initialization method of "Teacher" should accept an additional argument, "subject", and call the parent's (super) initialization method.
# Override the 'introduce()' method to print a sentence stating the teacher's name and what they teach.

class Teacher(SchoolMember):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    
    def introduce(self):
        print(f"This is teacher {self.name}, teaching {self.subject}.")

# TODO: Crank the engine and test the interstellar code by creating an instance of the Teacher class and calling its 'introduce()' method.

cosmo = Teacher("Cosmo", 18, "Space")
cosmo.introduce()