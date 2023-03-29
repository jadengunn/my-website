from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pyProj.urls')), # include the pyProj app's urls.py file
]