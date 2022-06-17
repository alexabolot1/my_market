from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='user_photos/', blank=True, verbose_name='аватар')
    age = models.PositiveIntegerField(null=True, verbose_name='возраст')

    def basket_price(self):
        return sum(item.product.price for item in self.basket.all())

    def basket_quantity(self):
        return sum(item.quantity for item in self.basket.all())
