from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import CustomUser, Post
from .forms import ProfileForm, CreatePostForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = CustomUser
        fields = ['email',]

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})
    
class LoginView(LoginView):
    template_name = 'login.html'

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'edit_profile.html', {'form': form})


 # blog/views.py (Update profile view)
@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'registration/profile.html', {'form': form})


class DetailView(DetailView):
    model = Post
    template_name = 'post_view.html'
    context_object_name = 'post'

class CreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_create.html'
    form_class = CreatePostForm
    success_url = '/list/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class UpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'

class DeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = 'posts/'
    context_object_name = 'post'

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  # Template for displaying all posts
    context_object_name = 'posts'
    ordering = ['-date_posted']  # Display latest posts first

# Display a single blog post
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'  # Template for displaying a single post

# Allow users to create a new post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the author to the logged-in user
        return super().form_valid(form)

# Allow post authors to update their posts
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user  # Ensure the author is the logged-in user
        return super().form_valid(form)

    # Ensure only the post's author can update it
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# Allow post authors to delete their posts
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post-list')  # Redirect to the post list after deletion
    template_name = 'blog/post_confirm_delete.html'

    # Ensure only the post's author can delete it
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
Step 2: Create and Configure Forms
For creating and updating blog posts, you will use Django’s ModelForm to handle form validation and rendering.

You don’t need to explicitly define a form class, as Django's class-based CreateView and UpdateView will automatically use a ModelForm if you provide the model and fields. The form will automatically validate input.

Step 3: Set Up Templates for Each Operation
Create the following templates in the blog/templates/blog/ directory:

3.1 Template for listing posts (post_list.html):
html
Copy code
{% extends "blog/base.html" %}

{% block content %}
  <h2>All Blog Posts</h2>
  {% for post in posts %}
    <div>
      <h3><a href="{% url 'post-detail' post.pk %}">{{ post.title }}</a></h3>
      <p>By {{ post.author }} on {{ post.date_posted }}</p>
      <p>{{ post.content|truncatewords:30 }}</p>
    </div>
  {% endfor %}
{% endblock %}
3.2 Template for viewing a single post (post_detail.html):
html
Copy code
{% extends "blog/base.html" %}

{% block content %}
  <article>
    <h2>{{ post.title }}</h2>
    <p>By {{ post.author }} on {{ post.date_posted }}</p>
    <p>{{ post.content }}</p>

    {% if user == post.author %}
      <a href="{% url 'post-update' post.pk %}">Edit</a>
      <a href="{% url 'post-delete' post.pk %}">Delete</a>
    {% endif %}
  </article>
{% endblock %}
3.3 Template for creating/editing posts (post_form.html):
html
Copy code
{% extends "blog/base.html" %}

{% block content %}
  <h2>{% if form.instance.pk %}Edit Post{% else %}Create New Post{% endif %}</h2>
  <form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">{% if form.instance.pk %}Update{% else %}Create{% endif %}</button>
  </form>
{% endblock %}
