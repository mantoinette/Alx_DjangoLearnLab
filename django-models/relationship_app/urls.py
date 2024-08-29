# urls.py
from django.urls import path
from .views import book_list, LibraryDetailView

urlpatterns = [
    path('books/', book_list, name='list_books'),  # Function-based view to list books
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view for library details
]
