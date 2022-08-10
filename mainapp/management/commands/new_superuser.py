from django.core.management.base import BaseCommand
from authapp.models import CustomUser


class Command(BaseCommand):
    help = 'Создание супер пользователя'

    def handle(self, *args, **kwargs):
        CustomUser.objects.create_superuser(username='alex', email='alex@mail.com', password='django')
