from rest_framework import viewsets, permissions, filters
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def get_queryset(self):
        # Get the current user
        user = self.request.user
        
        # If the user is authenticated, show posts from users they follow
        if user.is_authenticated:
            following_users = user.following.all()  # Assuming `following` is a ManyToMany field on CustomUser
            return Post.objects.filter(author__in=following_users).order_by('-created_at')

        # If not authenticated, return all posts
        return Post.objects.all().order_by('-created_at')

    def perform_create(self, serializer):
        # Automatically associate the post with the user making the request
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Automatically associate the comment with the user making the request
        serializer.save(author=self.request.user)
