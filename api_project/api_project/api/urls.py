# api/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookListCreateView.as_view(), name='book-list-create'),
    # Add more paths as needed
]
