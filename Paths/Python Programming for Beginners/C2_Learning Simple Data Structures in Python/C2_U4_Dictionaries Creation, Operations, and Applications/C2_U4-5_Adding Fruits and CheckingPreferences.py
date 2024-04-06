# A dictionary storing student's name and favorite fruit
student_fruit = {"Alice": "Apple", "Bob": "Banana", "Dean": "Orange"}

# TODO: Add Charlie's favorite fruit 'Cherries' to our dictionary
student_fruit["Charlie"] = "Cherries" 

# TODO: Check if Dean's favorite fruit is Durian and print True or False
# Make sure the code works even if Dean's name is removed from the dictionary
print(f"Dean's favorite fruit is Durian? {student_fruit.get('Dean',0) == 'Durian'}")


# This will show the updated student-favorite fruit pairs 
print(student_fruit)