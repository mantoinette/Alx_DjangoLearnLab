from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, CustomAuthToken, FollowViewSet

# Create a router for the FollowViewSet
router = DefaultRouter()
router.register(r'users', FollowViewSet, basename='user')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),

    # Custom paths for follow and unfollow actions using user_id
    path('follow/<int:user_id>/', FollowViewSet.as_view({'post': 'follow'}), name='follow-user'),
    path('unfollow/<int:user_id>/', FollowViewSet.as_view({'post': 'unfollow'}), name='unfollow-user'),

    # Include all router-generated URLs for standard actions
    path('', include(router.urls)),
]
