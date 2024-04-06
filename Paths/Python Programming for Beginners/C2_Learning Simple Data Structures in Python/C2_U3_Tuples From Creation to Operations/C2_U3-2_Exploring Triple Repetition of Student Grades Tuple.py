# Tuple of students with their respective grades
student_grades = (("Mary", 85), ("John", 78), ("Tom", 92), ("Emily", 88), ("Sam", 76))

# Tuple of additional students and their respective grades
additional_students = (("Mike", 81), ("Alex", 74))

# Concatenating tuples
all_students = student_grades + additional_students

# TODO: repeat `all_students` three times and print it
all_students *= 3

# Print the concatenated tuple
print(all_students)