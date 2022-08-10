from django.db import models

from mainapp.models import Product


class Order(models.Model):
    FORMING = 'F'
    READY = 'R'
    CANCELED = 'C'
    SENT = 'S'

    STATUS_CHOICES = (
        (FORMING, 'формируется'),
        (READY, 'готов'),
        (CANCELED, 'отменен'),
        (SENT, 'отправлен'),
    )

    create_data = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    update_data = models.DateTimeField(auto_now=True, verbose_name='дата обновления')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='статус', default=FORMING)
    is_active = models.BooleanField(default=True, verbose_name='активный')

    class Meta:
        ordering = ('-create_data',)
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

    @property
    def is_forming(self):
        return self.status == self.FORMING


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                             on_delete=models.CASCADE,
                             related_name='order',
                             verbose_name='Заказ')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    quantity = models.PositiveIntegerField(default=0, verbose_name='количество')
    create_data = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    update_data = models.DateTimeField(auto_now=True, verbose_name='дата обновления')

    @property
    def product_cost(self):
        return self.product.price * self.quantity
