<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test, permission_required
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, DetailView
from .models import Book, Library
from .forms import BookForm
from django.contrib.auth.forms import UserCreationForm

# Book List View
def book_list_view(request):
    """Retrieves all books and renders a template displaying the list."""
    books = Book.objects.all()  # Fetch all book instances from the database
    context = {'book_list': books}  # Create a context dictionary with book list
=======
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib import messages
from django.views.generic.detail import DetailView
from .models import Book, Library, UserProfile

# Helper function to check user roles
def check_role(user, role):
    if hasattr(user, 'userprofile'):
        return user.userprofile.role == role
    return False

# Book list view
def book_list_view(request):
    books = Book.objects.all()
    context = {'book_list': books}
>>>>>>> 95764bc777a695a85556049397d21638f8a56519
    return render(request, 'relationship_app/list_books.html', context)

# Library Details View
class LibraryDetailView(DetailView):
    """A class-based view for displaying details of a specific library."""
    model = Library
    template_name = 'relationship_app/library_detail.html'

<<<<<<< HEAD
    def get_context_data(self, **kwargs):
        """Injects additional context data specific to the library."""
        context = super().get_context_data(**kwargs)  # Get default context data
        library = self.get_object()  # Retrieve the current library instance
        context['average_rating'] = library.get_average_rating()  # Example additional data
        return context

# User Login View
class CustomLoginView(LoginView):
    template_name = 'authentication/login.html'
    redirect_authenticated_user = True
=======
# User login view
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to home after login
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

# User logout view
@login_required
def user_logout(request):
    logout(request)
    return redirect('home')  # Redirect to home after logout
>>>>>>> 95764bc777a695a85556049397d21638f8a56519

# User Logout View
class CustomLogoutView(LogoutView):
    template_name = 'authentication/logout.html'

# User Registration View
class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'authentication/register.html'
    success_url = reverse_lazy('login')

# Add Book View
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
<<<<<<< HEAD
            form.save()
            return redirect('book_list')
=======
            user = form.save()
            # Optionally, you can set the role here if you have a field in the form
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')
>>>>>>> 95764bc777a695a85556049397d21638f8a56519
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})

<<<<<<< HEAD
# Edit Book View
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/edit_book.html', {'form': form})

# Delete Book View
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'books/delete_book.html', {'book': book})

# Role-Based Views
def check_role(user, role):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == role

=======
# Admin view
>>>>>>> 95764bc777a695a85556049397d21638f8a56519
@user_passes_test(lambda user: check_role(user, 'Admin'))
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

<<<<<<< HEAD
=======
# Librarian view
>>>>>>> 95764bc777a695a85556049397d21638f8a56519
@user_passes_test(lambda user: check_role(user, 'Librarian'))
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

<<<<<<< HEAD
=======
# Member view
>>>>>>> 95764bc777a695a85556049397d21638f8a56519
@user_passes_test(lambda user: check_role(user, 'Member'))
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
