from django.urls import path

from ordersapp.views import OrderList, OrderCreate

app_name = 'ordersapp'

urlpatterns = [
    path('', OrderList.as_view(), name='order_list'),
    path('create/', OrderCreate.as_view(), name='order_create'),
]
