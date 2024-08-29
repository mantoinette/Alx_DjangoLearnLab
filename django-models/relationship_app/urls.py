from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import book_list, LibraryDetailView, user_register

urlpatterns = [
    path('books/', book_list, name='list_books'),  # Function-based view to list books
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view for library details
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),  # Django built-in login view
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),  # Django built-in logout view
    path('register/', user_register, name='register'),  # Custom registration view
]


