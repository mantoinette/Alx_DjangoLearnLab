from django.urls import path
from .views import book_list, library_list

urlpatterns = [
    path('books/', book_list, name='list_books'),  # For the function-based view
    path('library/<int:pk>/', library_list.as_view(), name='library_detail'),  # For the class-based view
]
