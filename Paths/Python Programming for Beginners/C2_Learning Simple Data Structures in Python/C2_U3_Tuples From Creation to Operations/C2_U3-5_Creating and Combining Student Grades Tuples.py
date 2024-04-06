# TODO: Create a nested tuple of student names and their grades
student_grade = (("Ada", 85), ("Bob", 88), ("Cosmo", 100))
# TODO: Merge it with an additional nested tuple containing other students' grades
student_grade += (("Dan",  70), ("Echo", 77), ("Mark", 80),)
# TODO: Print the combined tuple  
print(student_grade)
# TODO: Check if a student named "Mark" with a grade of "80" is in the combined tuple 
print(("Mark",80) in student_grade)