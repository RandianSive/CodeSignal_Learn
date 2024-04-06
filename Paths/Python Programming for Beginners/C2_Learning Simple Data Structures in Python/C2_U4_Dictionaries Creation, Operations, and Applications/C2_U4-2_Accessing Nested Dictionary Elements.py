school = {
    "students": {
        "Alice": {
            "age": 12, 
            "subjects": ["Math", "Science", "English"]
        },
        "Bob": {
            "age": 13, 
            "subjects": ["Math", "English", "History"]
        }
    },
    "teachers": {
        "Ms. Davis": {
            "subjects": ["Math", "Science"]
        },
        "Mr. Lee": {
            "subjects": ["English", "History"]
        }
    }
}

print(school["students"]["Alice"]["subjects"])
print(school["teachers"]["Mr. Lee"]["subjects"])