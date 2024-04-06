# A dictionary storing the classroom number as keys and the number of chairs in each room as values
classroom_info = {"Classroom 1": 20, "Classroom 2": 30, "Classroom 3": 25}

# Check if "Classroom 4" exists in the dictionary
if "Classroom 4" in classroom_info:
    print("Classroom 4 does exist. It has", classroom_info["Classroom 4"], "chairs.")
else:
    print("There's no data about Classroom 4.")

    
# Add 20 chairs to "Classroom 4"
classroom_info["Classroom 4"] = classroom_info.get("Classroom 4", 0) + 20
print(classroom_info)  # Expected Output: {'Classroom 1': 20, 'Classroom 2': 30, 'Classroom 3': 25, 'Classroom 4': 20}