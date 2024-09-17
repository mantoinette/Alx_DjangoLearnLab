from django import forms
from .models import Profile, Post, Comment  # Import the Comment model
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['email', 'bio', 'picture']

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

# Add CommentForm
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment  # Specify the Comment model
        fields = ['content']  # Allow users to input comment content
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
