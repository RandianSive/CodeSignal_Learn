# let's assume we have a string with book names separated by commas
book_string = "The Da Vinci Code,Angels & Demons,The Lost Symbol,Inferno,Origin"

# Using the split() method, we can convert this string to a list of book names
book_list = book_string.split(',')

# Let's join the list into a string again, but this time separated by a semicolon.
separated_string = '; '.join(book_list)
print(separated_string)