#imports
from django.contrib import admin
from django.urls import path, include

#--------------------------------------------------------------------------------------------------
#Path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('content.urls')),
]