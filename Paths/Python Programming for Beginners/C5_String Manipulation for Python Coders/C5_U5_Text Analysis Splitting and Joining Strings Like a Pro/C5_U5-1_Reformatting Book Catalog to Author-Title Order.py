text = """
1984 - George Orwell
To Kill a Mockingbird - Harper Lee
The Great Gatsby - F. Scott Fitzgerald
"""

lines = text.split("\n")[1:-1]
new_catalog = []
for line in lines:
  title, author = line.split(" - ")
  new_catalog.append(f"Author: {author}, Title: {title}")

new_text = "\n".join(new_catalog)
print(new_text)