from django.contrib import admin
from django.urls import path, include
from .views import list_books

urlpatterns = [
    path('admin/', admin.site.urls),
    path('relationship/', include('relationship_app.urls')),  # Include URLs from relationship_app
]
