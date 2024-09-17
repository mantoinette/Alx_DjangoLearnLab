from django import forms
from .models import Profile, Post
from django.contrib.auth.models import User
from django import Tag, Post
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['email', 'bio', 'picture']
class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(),  # Tag input widget
        }

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'})


        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class PostForm(forms.ModelForm):
    tags = forms.CharField()  # Add this line to handle tags as a comma-separated string

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def save(self, commit=True):
        instance = super().save(commit=False)
        tag_names = self.cleaned_data['tags'].split(',')  # Split by commas
        tags = [Tag.objects.get_or_create(name=tag_name.strip())[0] for tag_name in tag_names]
        if commit:
            instance.save()
            instance.tags.set(tags)
        return instance
