from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentCreateView,
    CommentDeleteView,
    CommentUpdateView,
    PostByTagListView  # Add this import
)

urlpatterns = [
    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),

    # Post URLs
    path('posts/', PostListView.as_view(), name='posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # Comment URLs
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='new_comment'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),

    # Search URL
    path('search/', views.search_posts, name='search-posts'),

    # For filtering posts by tag
    path('tags/<slug:tag_slug>/', views.PostByTagListView.as_view(), name='posts-by-tag'),  # Add this path
]
