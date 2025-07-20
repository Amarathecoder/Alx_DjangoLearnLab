# Import the models
from relationship_app.models import Author, Book, Library, Librarian

def main():
    library_name = "National Library"
    author_name='Chinua Achebe'
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)
    print("Books by Chinua Achebe:")
    for book in books_by_author:
        print(f"- {book.title}")

    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()
    print("\nBooks in National Library:")
    for book in books_in_library:
        print(f"- {book.title}")

    librarian = Librarian.objects.get(library=library)
    print(f"\nLibrarian for National Library: {librarian.name}")

if __name__ == "__main__":
    main()