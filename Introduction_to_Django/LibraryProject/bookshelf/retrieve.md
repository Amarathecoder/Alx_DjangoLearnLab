# Retrieve a Book

```python
from bookshelf.models import Book
retrieved_book = Book.objects.get(id=book.id)
retrieved_book
