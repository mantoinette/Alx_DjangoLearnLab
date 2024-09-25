from rest_framework import status, permissions, viewsets, filters, generics
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.response import Response
from posts.models import Post, Like, Comment
from notifications.models import Notification
from .serializers import PostSerializer, CommentSerializer
from django.shortcuts import get_object_or_404  # Correct import


# View for liking a post
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)  # Fetch the post by its ID
    user = request.user

    # Ensure Like.objects.get_or_create is used to avoid duplicate likes
    like, created = Like.objects.get_or_create(user=user, post=post)  # Ensures only one like per user per post

    if created:  # If a new like was created
        # Create a notification for the post author
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
    post = get_object_or_404(Post, pk=pk)  # Fetch the post by its ID
    user = request.user
    like = Like.objects.filter(user=user, post=post)  # Find the like

    if like.exists():  # If the like exists, delete it
        like.delete()
        return Response({'message': 'Post unliked'}, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({'error': 'Post not liked yet'}, status=status.HTTP_400_BAD_REQUEST)

# ViewSet for handling posts
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')  # Get all posts ordered by creation date
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
        following_users = request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)

# ViewSet for handling comments
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Automatically associate the comment with the user making the request
        serializer.save(author=self.request.user)
