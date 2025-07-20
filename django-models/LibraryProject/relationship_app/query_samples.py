import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

# Import the models
from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
author_name = "Chinua Achebe"
try:
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)
    print(f"Books by {author_name}:")
    for book in books_by_author:
        print(f"- {book.title}")
except Author.DoesNotExist:
    print(f"No author found with name {author_name}")

# 2. List all books in a specific library
library_name = "National Library"
try:
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()
    print(f"\nBooks in {library_name}:")
    for book in books_in_library:
        print(f"- {book.title}")
except Library.DoesNotExist:
    print(f"No library found with name {library_name}")

# 3. Retrieve the librarian for a specific library
try:
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library_name)  # thanks to OneToOne relationship
    print(f"\nLibrarian managing {library_name}: {librarian.name}")
except Library.DoesNotExist:
    print(f"No library found with name {library_name}")
except Librarian.DoesNotExist:
    print(f"No librarian assigned to {library_name}")
