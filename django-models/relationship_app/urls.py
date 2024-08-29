from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import book_list, LibraryDetailView, user_register, user_login, user_logout

urlpatterns = [
    path('books/', book_list, name='list_books'),  # Function-based view to list books
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view for library details
    path('login/', user_login, name='login'),  # Custom login view
    path('logout/', user_logout, name='logout'),  # Custom logout view
    path('register/', user_register, name='register'),  # Custom registration view
]
