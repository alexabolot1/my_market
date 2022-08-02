import hashlib
import random
import datetime

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.timezone import now


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='user_photos/', blank=True, verbose_name='аватар')
    age = models.PositiveIntegerField(verbose_name='возраст', default=18)
    user_activation_key = models.CharField(max_length=128, blank=True, verbose_name='ключ активации')

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ['-is_active']

    @property
    def is_activation_key_expires(self):
        """
        Проверяет истекло ли время для авторизации пользователя
        :return: True, если время вышло
        """
        return now() - self.date_joined > datetime.timedelta(hours=48)

    def set_activation_key(self):
        """
        Получает ключ активации с помощью соли
        """
        salt = hashlib.sha1(str(random.random()).encode('utf8')).hexdigest()[:6]
        self.user_activation_key = hashlib.sha1((self.email + salt).encode('utf8')).hexdigest()

    def send_confirm_email(self):
        """
        Формирует ссылку для авторизации
        :return: send_mail - отправляет ссылку для авторизации на email пользователю.
        """
        verify_link = reverse('authapp:verify', kwargs={'email': self.email,
                                                        'user_activation_key': self.user_activation_key})
        subject = f'Подтверждение учетной записи {self.username}'
        message = f'Для подтверждения учетной записи {self.username} на портале ' \
                  f'{settings.DOMAIN_NAME} перейдите по ссылке: {settings.DOMAIN_NAME}{verify_link}'
        return send_mail(subject, message, settings.EMAIL_HOST_USER, [self.email], fail_silently=False)

    def basket_price(self):
        """
        :return: сумма корзины пользователя
        """
        return sum(item.product_cost for item in self.basket.all())

    def basket_quantity(self):
        """
        :return: количество товаров в корзине пользователя
        """
        return sum(item.quantity for item in self.basket.all())
