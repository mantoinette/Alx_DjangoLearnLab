from django.urls import path
from .views import LoginView, register, LogoutView, profile, edit_profile, CreateView, UpdateView, DetailView, DeleteView, ListView

urlpatterns = [
path('posts/', PostListView.as_view(), name='posts'),
path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
path('post/new/', PostCreateView.as_view(), name='post-create'),
path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),


]
