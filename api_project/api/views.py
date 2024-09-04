
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from .permissions import IsOwnerOrReadOnly

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
