# A nested dictionary with students as keys & their subjects and marks as values
students = {
    "Alice": {"Maths": 90, "Science": 85, "English": 88},
    "Bob": {"Maths": 80, "Science": 75, "English": 93},
    "Charlie": {"Maths": 88, "Science": 78, "English": 79}
}

# Accessing Alice's Science marks
# TODO: Directly print Alice's Science marks from the dictionary
print(students["Alice"]["Science"])

# Removing Charlie's English marks and print the updated dictionary
# TODO: Remove English marks for Charlie from the nested dictionary, print the removed English mark
# TODO: Print the updated dictionary with marks for Charlie after the previous removal
del students["Charlie"]["English"]
print(students)