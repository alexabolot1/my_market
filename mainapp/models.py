from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='имя', max_length=40, db_index=True)
    description = models.TextField(verbose_name='описание', blank=True)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='имя', max_length=40, db_index=True)
    description = models.TextField(verbose_name='описание', blank=True)
    image = models.ImageField(verbose_name='изображение', upload_to='products_images', blank=True)
    price = models.DecimalField(verbose_name='цена', max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(verbose_name='количество', default=0)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    @staticmethod
    def get_items():
        return Product.objects.filter(is_active=True).order_by('name')

    def __str__(self):
        return f'{self.name} ({self.category.name})'
