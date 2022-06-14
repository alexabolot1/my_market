from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='user_photos/', blank=True, verbose_name='аватар')
    age = models.PositiveIntegerField(null=True, verbose_name='возраст')
