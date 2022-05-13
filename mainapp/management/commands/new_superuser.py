from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = u'Create superuser'

    def handle(self, *args, **kwargs):
        User.objects.create_superuser(username='alex', email='alex@mail.com', password='django')
