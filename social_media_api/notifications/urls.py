# notifications/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_notifications, name='list_notifications'),
    path('<int:pk>/mark-read/', views.mark_as_read, name='mark_as_read'),
]
