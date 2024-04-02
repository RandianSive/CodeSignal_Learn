# Define book titles and author names
book_title_1 = "The Lord of the Rings"
book_author_1 = "J.R.R. Tolkien"
book_title_2 = "The Fellowship of the Ring"
book_author_2 = "J.R.R. Tolkien"

# Compare whether the two book titles are the same
same_book = book_title_1 == book_title_2
print("Are both books the same? " + str(same_book))

# Compare whether the two authors are the same
same_author = book_author_1 == book_author_2
print("Are both authors the same? " + str(same_author))

# Combine title and author using concatenation
books_info = 'Book: ' + book_title_1 + ', Author: ' + book_author_1
print(books_info)