from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from posts.models import Post, Like
from notifications.models import Notification

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])  # Ensure the user is authenticated
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)  # Retrieve the post or return 404
    user = request.user

    # Check or create a like for the user and post
    like, created = Like.objects.get_or_create(user=user, post=post)

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
