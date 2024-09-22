from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, like_post, unlike_post, list_notifications, mark_as_read

# Create a router for PostViewSet and CommentViewSet
router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    # Include all router-generated URLs for posts and comments
    path('', include(router.urls)),

    # Custom path for the feed, which shows posts from followed users
    path('feed/', PostViewSet.as_view({'get': 'feed'}), name='post-feed'),
    
    # Paths for liking and unliking posts
    path('posts/<int:pk>/like/', like_post, name='like_post'),
    path('posts/<int:pk>/unlike/', unlike_post, name='unlike_post'),

    # Paths for notifications
    path('notifications/', list_notifications, name='list_notifications'),
    path('notifications/<int:pk>/mark-read/', mark_as_read, name='mark_as_read'),
]
