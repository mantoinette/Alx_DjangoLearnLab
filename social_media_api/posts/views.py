from .serializers import PostSerializer, CommentSerializer
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework import status, viewsets, permissions, filters
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from posts.models import Post, Like
from notifications.models import Notification

# View for liking a post
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])  # Ensure the user is authenticated
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user = request.user

    # Check or create a like for the user and post
    like, created = Like.objects.get_or_create(user=user, post=post)

    if created:  # If a new like was created
        Notification.objects.create(
            recipient=post.author,
            actor=user,
            verb='liked',
            target=post
        )
        return Response({'message': 'Post liked'}, status=status.HTTP_201_CREATED)
    else:
        return Response({'error': 'Post already liked'}, status=status.HTTP_400_BAD_REQUEST)

# View for unliking a post
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])  # Ensure the user is authenticated
def unlike_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user = request.user
    like = Like.objects.filter(user=user, post=post)
    
    if like.exists():
        like.delete()
        return Response({'message': 'Post unliked'}, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({'error': 'Post not liked yet'}, status=status.HTTP_400_BAD_REQUEST)

# ViewSet for handling posts
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def feed(self, request):
        following_users = request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)

# Remember to implement CommentViewSet and any other necessary views.
