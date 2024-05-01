# Let's create a very simple book recommendation function

book_companion = 'Blindness - Jose Saramago, Crime and Punishment - Fyodor Dostoevsky, 1984 - George Orwell'

book_list = book_companion.split(", ")
favorite_book = book_list[2]
title, author = favorite_book.split(" - ")
print(f"My favorite book is '{title}' authored by {author}. I highly recommend it!")