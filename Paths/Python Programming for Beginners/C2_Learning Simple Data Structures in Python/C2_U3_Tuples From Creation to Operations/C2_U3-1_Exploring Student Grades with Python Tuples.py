# Tuple of considered students and their respective grades
students_grades = (("Mary", 75), ("John", 80), ("Steve", 85), ("Susan", 90))

# Accessing the first student's name and grade
first_student = students_grades[0]
print("The first student is", first_student[0], "and their grade is", first_student[1])

# Counting occurrence of a specific grade in the tuple
# Note: int(True) == 1, int(False) == 0
grade = 85
occurrences = int(students_grades[0][1] == 85) + int(students_grades[1][1] == 85) + int(students_grades[2][1] == 85) + int(students_grades[3][1] == 85)
print("The number of students with grade", grade, "is:", occurrences)