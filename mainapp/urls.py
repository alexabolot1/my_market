from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.main, name='index'),
    path('products', mainapp.products, name='products'),
    path('contacts', mainapp.contacts, name='contacts'),
    path('product_details/<int:pk>', mainapp.product, name='product')
]
