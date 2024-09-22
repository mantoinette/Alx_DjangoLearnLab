# posts/views.py

from rest_framework import status, viewsets, permissions, filters
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from posts.models import Post, Like, Comment
from notifications.models import Notification
from .serializers import PostSerializer, CommentSerializer

# View for liking a post
@api_view(['POST'])
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user = request.user
    if not post.likes.filter(user=user).exists():
        Like.objects.create(user=user, post=post)
        # Create a notification
        Notification.objects.create(
            recipient=post.author,  # The author of the post
            actor=user,
            verb='liked',
            target=post
        )
        return Response({'message': 'Post liked'}, status=status.HTTP_201_CREATED)
    else:
        return Response({'error': 'Post already liked'}, status=status.HTTP_400_BAD_REQUEST)

# View for unliking a post
@api_view(['POST'])
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
        # Automatically associate the post with the user making the request
        serializer.save(author=self.request.user)

    # Custom feed action to get posts from followed users
    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def feed(self, request):
        # Get users followed by the current user
        following_users = request.user.following.all()
        # Filter posts by those users
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)

# You would also need to define the CommentViewSet and other necessary views here.
