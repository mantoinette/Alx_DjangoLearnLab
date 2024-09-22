from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, CustomAuthToken, FollowViewSet

router = DefaultRouter()
router.register(r'users', FollowViewSet, basename='user')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('', include(router.urls)),
]
