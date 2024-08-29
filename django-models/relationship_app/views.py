# views.py
from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library

def book_list(request):
    """Retrieves all books and renders a template displaying the list."""
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
