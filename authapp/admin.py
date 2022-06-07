from django.contrib import admin

# Register your models here.
from authapp.models import CustomUser

admin.site.register(CustomUser)
