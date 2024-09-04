# api/urls.py
from django.urls import path
from . import views

urlpatterns = [
  path('books/', BookList.as_view(), name='book-list'),
]
