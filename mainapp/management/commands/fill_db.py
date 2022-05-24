import json

from django.core.management.base import BaseCommand
from mainapp.models import Product, Category


def load_from_json(file_name):
    with open(file_name, encoding='utf-8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    help = 'Заполнение данными категорий и продуктов'

    def handle(self, *args, **options):
        items = load_from_json('mainapp/json/categories.json')
        for item in items:
            Category.objects.create(**item)

        items = load_from_json('mainapp/json/products.json')
        for item in items:
            category = Category.objects.get(name=item['category'])
            item['category'] = category
            Product.objects.create(**item)

        # # len(Product.objects.filter(category=1))
        # # Product.objects.filter(category=1).count()
        # if not ShopUser.objects.filter(username='django').exists():
        #     ShopUser.objects.create_superuser('django', 'django@gb.local', 'geekbrains')
