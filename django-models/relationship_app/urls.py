from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.book_list, name='home'),  # Home page view
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # Login view
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  # Logout view
    path('register/', views.user_register, name='register'),  # Register view

    # Role-specific views
    path('admin-view/', views.admin_view, name='admin_view'),  # Admin view
    path('librarian-view/', views.librarian_view, name='librarian_view'),  # Librarian view
    path('member-view/', views.member_view, name='member_view'),  # Member view
]
