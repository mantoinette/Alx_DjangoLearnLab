from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import user_passes_test  # Import this
from .models import Book, Library

# List all books
def book_list(request):
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, 'relationship_app/list_books.html', context)

# Detail view for a library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

# Login view
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list_books')
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

# Logout view
def user_logout(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')

# Registration view
def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Role-Based Access Control Views

# Check if the user is an Admin
def is_admin(user):
    return user.userprofile.role == 'Admin'

# Check if the user is a Librarian
def is_librarian(user):
    return user.userprofile.role == 'Librarian'

# Check if the user is a Member
def is_member(user):
    return user.userprofile.role == 'Member'

# Admin view, accessible only by Admin users
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')  # Adjust the template path as needed

# Librarian view, accessible only by Librarian users
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')  # Adjust the template path as needed

# Member view, accessible only by Member users
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')  # Adjust the template path as needed
