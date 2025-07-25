from relationship_app.models import Author, Book, Library

# Add Authors
achebe = Author.objects.create(name="Chinua Achebe", biography="Best known for Things Fall Apart.")
adichie = Author.objects.create(name="Chimamanda Ngozi Adichie", biography="Author of Purple Hibiscus and Half of a Yellow Sun.")
soyinka = Author.objects.create(name="Wole Soyinka", biography="Nobel Laureate, playwright, and poet.")

# Add Library
lagos_lib = Library.objects.create(name="Lagos Central Library", location="Broad Street, Lagos")

# Add Books
Book.objects.create(title="Things Fall Apart", author=achebe, publication_year=1958, library=lagos_lib)
Book.objects.create(title="Purple Hibiscus", author=adichie, publication_year=2003, library=lagos_lib)
Book.objects.create(title="Death and the King's Horseman", author=soyinka, publication_year=1975, library=lagos_lib)
