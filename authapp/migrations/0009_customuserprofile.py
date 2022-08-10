# Generated by Django 3.2.8 on 2022-08-10 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0008_alter_customuser_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='authapp.customuser')),
                ('tagline', models.CharField(blank=True, max_length=126, verbose_name='теги')),
                ('about_me', models.TextField(blank=True, verbose_name='о себе')),
                ('gender', models.CharField(blank=True, choices=[('M', 'мужской'), ('W', 'женский')], max_length=1, verbose_name='пол')),
            ],
        ),
    ]
