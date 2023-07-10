from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apppsy.urls')),
    path('', include('usersapp.urls')),
]