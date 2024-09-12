from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# User registration form extending the default UserCreationForm
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()  # Add email field to the registration form

    class Meta:
        model = User  # Use the built-in User model
        fields = ['username', 'email', 'password1', 'password2']  # Fields to be displayed in the form

# Form for updating user profile information (username and email)
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()  # Include email field

    class Meta:
        model = User  # Use the User model
        fields = ['username', 'email']  # Fields available for update
