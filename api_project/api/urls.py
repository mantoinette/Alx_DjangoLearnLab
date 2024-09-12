from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookList
from rest_framework.authtoken.views import obtain_auth_token

# Create a router and register the BookViewSet
router = DefaultRouter()
router.register(r'books', BookViewSet)

# Include the router URLs and the custom view in your urlpatterns
urlpatterns = [
    path('', include(router.urls)),
    path('api/books-list/', BookList.as_view(), name='book-list'),  # Adding the custom BookList view
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
