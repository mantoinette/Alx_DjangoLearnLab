from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

# Create a router for PostViewSet and CommentViewSet
router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    # Include all router-generated URLs for posts and comments
    path('', include(router.urls)),

    # Custom path for the feed, which shows posts from followed users
    path('feed/', PostViewSet.as_view({'get': 'feed'}), name='post-feed'),
]
