# Generated by Django 3.2.8 on 2022-06-16 17:30

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0002_alter_product_image'),
        ('basketapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Basket',
            new_name='BasketItem',
        ),
    ]
