# Generated by Django 3.2.8 on 2022-07-14 04:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0006_customuser_user_activation_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='registered',
        ),
    ]