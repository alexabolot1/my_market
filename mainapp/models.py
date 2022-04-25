from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='имя', max_length=40, db_index=True)
    description = models.TextField(verbose_name='описание', blank=True)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='имя', max_length=40, db_index=True)
    description = models.TextField(verbose_name='описание', blank=True)
    image = models.ImageField(verbose_name='изображение', upload_to='products/%Y/%m/%d', blank=True)
    price = models.DecimalField(verbose_name='цена', max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(verbose_name='количество')
    is_active = models.BooleanField(verbose_name='активна', default=True)

    class Meta:
        ordering = ('name',)

    @staticmethod
    def get_items():
        return Product.objects.filter(is_active=True).order_by('name')

    def __str__(self):
        return self.name
