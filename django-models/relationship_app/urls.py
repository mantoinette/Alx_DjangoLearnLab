from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.book_list_view, name='home'),  # Home page showing list of books
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # Library detail view

    # Authentication URLs
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', views.user_logout, name='logout'),  # Using custom logout view
    path('register/', views.user_register, name='register'),

    # Role-specific views
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
]
