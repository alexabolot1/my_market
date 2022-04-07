from django.contrib import admin
from django.urls import path, include

import mainapp.views as mainapp


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls', namespace='acc'))
]
