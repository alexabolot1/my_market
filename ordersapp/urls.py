from django.urls import path

from ordersapp.views import OrderList, OrderCreate, OrderUpdate, OrderDetail

app_name = 'ordersapp'

urlpatterns = [
    path('', OrderList.as_view(), name='order_list'),
    path('create/', OrderCreate.as_view(), name='order_create'),
    path('read/<int:pk>', OrderDetail.as_view(), name='order_detail'),
    path('update/<int:pk>', OrderUpdate.as_view(), name='order_update')
]
