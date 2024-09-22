from django.urls import path
from .views import list_notifications, mark_as_read

urlpatterns = [
    path('', list_notifications, name='list_notifications'),  # List notifications
    path('<int:pk>/mark-read/', mark_as_read, name='mark_as_read'),  # Mark a specific notification as read
]
