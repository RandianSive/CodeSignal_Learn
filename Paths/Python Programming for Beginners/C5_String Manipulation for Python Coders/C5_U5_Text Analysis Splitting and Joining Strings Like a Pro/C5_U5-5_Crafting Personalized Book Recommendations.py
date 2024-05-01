# List of books (title - author)
book_list = "Introduction to Python - Guido van Rossum,Mastering String Operations - Cosmo,Coding in Cosmos - Ada Lovelace"

# TODO: Split the book_list into separate books (Hint: Use the split() method)

list_of_book = book_list.split(",")

# TODO: For each book, split it into a title and author.
# Then, print a recommendation and a link to buy each book.
# Construct any valid web link that includes a book title

for book in list_of_book:
    try:
        title, author = book.split(" - ")
        print(f"Recommend book: {title} by {author}. For more information, please check: https://www.google.com/search?q={title.replace(' ', '_')}")
    except:
        print("Format error, please check.")