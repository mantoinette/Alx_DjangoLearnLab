from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('api/', include('posts.urls')),
    path('api/notifications/', include('notifications.urls')),  # Include notifications URLs
]

