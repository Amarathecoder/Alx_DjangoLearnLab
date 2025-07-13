# CRUD Operations for Book Model

---

## Create
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
```

**Output:**
```
<Book: 1984 by George Orwell>
```

## Retrieve
```python
retrieved_book = Book.objects.get(id=book.id)
retrieved_book
```

**Output:**
```
<Book: 1984 by George Orwell>
```

## Update
```python
book.title = "Nineteen Eighty-Four"
book.save()
book
```

**Output:**
```
<Book: Nineteen Eighty-Four by George Orwell>
```

## Delete
```python
book.delete()
```

**Output:**
```
(1, {'bookshelf.Book': 1})
```
