
from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('book/', views.book_list, name='book'),
    path('library/', views.library_list.as_view(), name='library'),
]

