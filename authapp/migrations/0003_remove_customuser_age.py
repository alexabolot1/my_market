# Generated by Django 3.2.8 on 2022-06-12 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_auto_20220612_1629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='age',
        ),
    ]
