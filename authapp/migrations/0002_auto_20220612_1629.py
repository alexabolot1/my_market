# Generated by Django 3.2.8 on 2022-06-12 11:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='age',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(18)], verbose_name='возраст'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='user_photos/', verbose_name='аватар'),
        ),
    ]
