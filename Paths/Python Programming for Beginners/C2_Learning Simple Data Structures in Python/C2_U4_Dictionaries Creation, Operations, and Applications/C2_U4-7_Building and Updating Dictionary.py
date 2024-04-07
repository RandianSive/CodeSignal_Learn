# TODO: Create a dictionary named 'student_subjects' that stores students' names as keys and their favorite subjects as values
student_subjects = {"Ada": "Math","Bob": "Science","Cosmo": "Universe","Eve":"Math"}

# TODO: Add a new key-value pair for a new student, David, who likes History
student_subjects["David"] = "History"

# TODO: Verify if the new key-value pair has been added successfully by printing the 'student_subjects' dictionary.
print(student_subjects)

# TODO: Check if a student named "Eve" likes Math or not. If Eve likes Math, print "Eve likes Math!". If we don't have information about Eve's favorite subject or she doesn't like Math, print "We don't have information about Eve's favorite subject or she doesn't like Math."
print ("Eve likes Math!") if student_subjects.get("Eve") == "Math" else print("We don't have information about Eve's favorite subject or she doesn't like Math.")