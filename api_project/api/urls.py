from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

# Create a router and register the BookViewSet
router = DefaultRouter()
router.register(r'books', BookViewSet)

# Include the router URLs in your urlpatterns
urlpatterns = [
    path('', include(router.urls)),
]
