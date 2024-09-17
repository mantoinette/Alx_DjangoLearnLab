from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Set when the comment is first created
    updated_at = models.DateTimeField(auto_now=True)      # Updates every time the comment is saved

    def __str__(self):
        return self.content
      
class CustomUser(AbstractUser):
    username = models.CharField(unique=True, max_length=100)
    email = None
     


class Tag(models.Model):
    name = models.CharField(max_length=255)
   