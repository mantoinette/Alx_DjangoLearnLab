from rest_framework import status, permissions, viewsets, filters, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
# No need to import django.shortcuts.get_object_or_404
from posts.models import Post, Like, Comment
from notifications.models import Notification
from .serializers import PostSerializer, CommentSerializer

# View for liking a post
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def like_post(request, pk):
    post = generics.get_object_or_404(Post, pk=pk)  # Now using generics.get_object_or_404
    user = request.user

    like, created = Like.objects.get_or_create(user=user, post=post)  # This line is present

    if created:  # If a new like was created
        # Create a notification
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
@permission_classes([permissions.IsAuthenticated])
def unlike_post(request, pk):
    post = generics.get_object_or_404(Post, pk=pk)  # Now using generics.get_object_or_404
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
        # Automatically associate the post with the user making the request
        serializer.save(author=self.request.user)
