from django.core.management import BaseCommand

from authapp.models import CustomUser, CustomUserProfile


class Command(BaseCommand):
    help = 'Заполнение данными категорий и продуктов'

    def handle(self, *args, **options):
        for user in CustomUser.objects.filter(customuserprofile__isnull=True):
            CustomUserProfile.objects.create(user=user)

