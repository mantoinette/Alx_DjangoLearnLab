# notifications/views.py
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from notifications.models import Notification

@api_view(['GET'])
def list_notifications(request):
    notifications = request.user.notifications.filter(read=False)  # Unread notifications
    notification_data = [{
        'actor': notification.actor.username,
        'verb': notification.verb,
        'target': str(notification.target),
        'timestamp': notification.timestamp
    } for notification in notifications]
    return Response(notification_data, status=status.HTTP_200_OK)

@api_view(['POST'])
def mark_as_read(request, pk):
    try:
        notification = Notification.objects.get(pk=pk, recipient=request.user)
        notification.read = True
        notification.save()
        return Response({'message': 'Notification marked as read'}, status=status.HTTP_200_OK)
    except Notification.DoesNotExist:
        return Response({'error': 'Notification not found'}, status=status.HTTP_404_NOT_FOUND)
