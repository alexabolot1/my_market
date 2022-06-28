from django.urls import path
import basketapp.views as basketapp

app_name = 'basketapp'

urlpatterns = [
    path('', basketapp.index, name='index'),
    path('add/<int:product_pk>', basketapp.basket_add, name='add'),
    path('remove/<int:basket_item_pk>', basketapp.basket_remove, name='remove'),
    path('update/<int:basket_item_pk>/<int:basket_item_quantity>/', basketapp.basket_update)
]
