# Tuple of students with their respective grades
student_grades = (("Mary", 85), ("John", 78), ("Tom", 92), ("Emily", 88), ("Sam", 76))

# Concatenating tuples
additional_students = (("Mike", 81), ("Alex", 74))
all_students = student_grades + additional_students
print(all_students)    # Should print (('Mary', 85), ('John', 78), ('Tom', 92), ('Emily', 88), ('Sam', 76), ('Mike', 81), ('Alex', 74))

# Accessing tuple members using negative indexing
print(all_students[-1])  # Should print ('Alex', 74)

# Using 'in' to check for a student in the tuple
print(("Mike", 81) in all_students)  # Should print True

# Counting occurrence of a specific tuple in the tuple
print(all_students.count(("Mike", 81)))  # Should print 1