from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import book_list, LibraryDetailView, user_register

urlpatterns = [
    path('', book_list, name='home'),  # Home page route
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Library detail page
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # Login page
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  # Logout page
    path('register/', user_register, name='register'),  # Registration page
]
