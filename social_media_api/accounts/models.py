from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    
    # Followers and Following Relationships
    followers = models.ManyToManyField('self', symmetrical=False, related_name='user_followers', blank=True)
    following = models.ManyToManyField('self', symmetrical=False, related_name='user_following', blank=True)

    def __str__(self):
        return self.username
