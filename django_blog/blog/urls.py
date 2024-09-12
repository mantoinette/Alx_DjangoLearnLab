from django.urls import path
from django.contrib.auth import views as auth_views  # Import built-in authentication views
from . import views

# URL patterns for authentication and profile management
urlpatterns = [
    path('register/', views.register, name='register'),  # URL for user registration
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),  # URL for login
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),  # URL for logout
    path('profile/', views.profile, name='profile'),  # URL for user profile page
    path('profile/update/', views.profile_update, name='profile_update'),  # URL for updating profile
]
