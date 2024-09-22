from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, CustomAuthToken, FollowViewSet

# Create a router for the FollowViewSet
router = DefaultRouter()
router.register(r'users', FollowViewSet, basename='user')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),

    # Custom paths for follow and unfollow actions, using user_id instead of pk
    path('users/<int:user_id>/follow/', FollowViewSet.as_view({'post': 'follow'}), name='follow-user'),
    path('users/<int:user_id>/unfollow/', FollowViewSet.as_view({'post': 'unfollow'}), name='unfollow-user'),

    # Include all router-generated URLs (for standard CRUD actions)
    path('', include(router.urls)),
]
