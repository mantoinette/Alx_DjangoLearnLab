from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.decorators import login_required

# View for user registration
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)  # Handle form submission
        if form.is_valid():  # If form is valid, save the user
            form.save()
            username = form.cleaned_data.get('username')  # Get the username from the form
            messages.success(request, f'Account created for {username}!')  # Display success message
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserRegisterForm()  # Show an empty form if it's a GET request
    return render(request, 'blog/register.html', {'form': form})  # Render the registration page

# View for user login (uses built-in AuthenticationForm)
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)  # Handle login form submission
        if form.is_valid():  # If the form is valid, authenticate the user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)  # Authenticate user
            if user is not None:
                login(request, user)  # Log the user in
                messages.success(request, f'You are now logged in as {username}')  # Success message
                return redirect('profile')  # Redirect to profile page
            else:
                messages.error(request, 'Invalid username or password')  # Error message
    else:
        form = AuthenticationForm()  # Show an empty login form
    return render(request, 'blog/login.html', {'form': form})  # Render the login page

# View for user profile (requires login)
@login_required
def profile(request):
    return render(request, 'blog/profile.html')  # Render the profile page

# View to update user profile (requires login)
@login_required
def profile_update(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)  # Handle form submission for profile update
        if form.is_valid():  # If the form is valid, save the updated profile
            form.save()
            messages.success(request, 'Your profile has been updated!')  # Success message
            return redirect('profile')  # Redirect to the profile page
    else:
        form = UserUpdateForm(instance=request.user)  # Pre-fill the form with current user data
    return render(request, 'blog/profile_update.html', {'form': form})  # Render the profile update page
