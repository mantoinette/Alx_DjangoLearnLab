from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
# Create your views here.
def book_list(request):
    """Retrieves all books and renders a template displaying the list."""
    books = Book.objects.all()  # Fetch all book instances from the database
    context = {'book_list': books}
    return render(request, 'relationship_app/list_books.html', context)

class library_list(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
