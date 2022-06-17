from django.contrib.auth import get_user_model
from django.db import models

from mainapp.models import Product


class BasketItem(models.Model):
    user = models.ForeignKey(get_user_model(),
                             on_delete=models.CASCADE,
                             related_name='basket',
                             verbose_name='Пользователь')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    quantity = models.PositiveIntegerField(default=0, verbose_name='количество')
    create_data = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    update_data = models.DateTimeField(auto_now=True, verbose_name='дата обновления')

    class Meta:
        verbose_name = 'корзина'
        verbose_name_plural = 'корзины'
