from django.shortcuts import render

# Create your views here.
from .models import Book

def book_list_view(request):
    books = Book.objects.select_related('author').all()
    context = {
        'books': books
    }
    return render(request, 'relationship_app/book_list.html', context)

from django.views.generic.detail import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()  # Using related_name from the Book model
        return context
