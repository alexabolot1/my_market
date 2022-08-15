# Generated by Django 3.2.8 on 2022-08-10 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainapp', '0003_auto_20220709_0814'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_data', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('update_data', models.DateTimeField(auto_now=True, verbose_name='дата обновления')),
                ('status', models.CharField(choices=[('F', 'формируется'), ('R', 'готов'), ('C', 'отменен'), ('S', 'отправлен')], default='F', max_length=1, verbose_name='статус')),
                ('is_active', models.BooleanField(default=True, verbose_name='активный')),
            ],
            options={
                'verbose_name': 'заказ',
                'verbose_name_plural': 'заказы',
                'ordering': ('-create_data',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='количество')),
                ('create_data', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('update_data', models.DateTimeField(auto_now=True, verbose_name='дата обновления')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='ordersapp.order', verbose_name='Заказ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.product', verbose_name='Продукт')),
            ],
        ),
    ]