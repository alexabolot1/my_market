from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import mainapp.views as mainapp
from my_market import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls', namespace='acc'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
