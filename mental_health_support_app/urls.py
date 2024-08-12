# mindsync/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mental_health_support_app.urls')),  # Include the app's URLs
]
