book_catalogue = "1984 - George Orwell, The Great Gatsby - F.Scott Fitzgerald, To Kill a Mockingbird - Harper Lee"
book_list = book_catalogue.split(", ")

reformatted_catalogue = []
for book in book_list:
    try:
        # TODO: Split each book into the title and the author
        # TODO: Reformat each description to "Author - Title" format and add to `reformatted_catalogue`
        # For example, "1984 - George Orwell" should become "George Orwell - 1984"
        title,author = book.split(" - ")
        reformatted_catalogue += (author + " - " + title),
            
    except ValueError:
        print("A book in your catalogue is not in correct format. Please, ensure the book and author are differentiated using ' - ' ")

# TODO: Join all book descriptions from 'reformatted_catalogue' into a single string, separating them using ", "
print(", ".join(reformatted_catalogue))