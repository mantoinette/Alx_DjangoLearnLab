from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
<<<<<<< HEAD
    path('', views.book_list_view, name='home'),
    path('', views.LibraryDetails_view, name='home'),
    "LogoutView.as_view(template_name="logut.html, 
    "LoginView.as_view(template_name="login.html"
    "views.register"
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
     path('admin/', admin_view, name='admin_view'),
    
    # URL for Librarian view
    path('librarian/', librarian_view, name='librarian_view'),
    
    # URL for Member view
    path('member/', member_view, name='member_view'),


     path('books/add/', views.add_book, name='add_book'),
    path('books/<int:pk>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:pk>/delete/', views.delete_book, name='delete_book'),
=======
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
>>>>>>> 95764bc777a695a85556049397d21638f8a56519
]
