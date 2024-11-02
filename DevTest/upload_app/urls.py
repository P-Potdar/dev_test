# DevTest/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('upload_app.urls')),
]

# upload_app/urls.py
from django.urls import path
from .views import upload_file

urlpatterns = [
    path('', upload_file, name='upload_file'),
]
