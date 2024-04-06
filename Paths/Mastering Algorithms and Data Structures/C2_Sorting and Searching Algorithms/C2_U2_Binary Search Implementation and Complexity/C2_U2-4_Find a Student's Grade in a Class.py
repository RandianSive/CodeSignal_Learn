# TODO: Given a sorted list of grades in a class, implement Binary Search on this list
grades = [35, 42, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

# TODO: Implement the Loop-based Binary Search function without recursion

# Loop-based Binary Search function
def binary_search_loop(grades, target):
    low = 0
    high = len(grades) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if grades[mid] == target:
            return mid  # Grade found at position mid
        elif grades[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1  # Grade not found

# TODO: Set a query for a student's grade for your search

# Query for a student's grade
grade_query = 65

# TODO: Invoke the Binary Search function. If you find the grade, print the position in the grade list; if not, print a not found message.

# Invoke the Binary Search function
position = binary_search_loop(grades, grade_query)

# Print the result
if position != -1:
    print(f"The grade {grade_query} is found at position {position} in the grade list.")
else:
    print(f"The grade {grade_query} is not found.")