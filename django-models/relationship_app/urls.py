from django.urls import path
from . import views
from .views import RegisterView, LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.book_list_view, name='home'),
    path('library/', LibraryDetailView.as_view(), name='library_detail'),

    path('login/', LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]

# Ensure the following view functions are placed in `views.py` or a relevant file

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def check_role(user, role):
    # Custom logic to check the user's role
    return user.groups.filter(name=role).exists()

# Admin view
@user_passes_test(lambda user: check_role(user, 'Admin'))
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian view
@user_passes_test(lambda user: check_role(user, 'Librarian'))
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member view
@user_passes_test(lambda user: check_role(user, 'Member'))
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
