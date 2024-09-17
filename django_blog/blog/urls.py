from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
     path('post/new/', views.PostCreateView.as_view(), name='post-create'),

    # Update an existing post
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),

    # Delete an existing post
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

]
