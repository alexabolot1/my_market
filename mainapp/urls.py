from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('products/', mainapp.products, name='products'),
    path('contacts/', mainapp.contacts, name='contacts'),
    path('category/<int:pk>', mainapp.category, name='category'),
    path('product_item/<int:pk>', mainapp.product_item, name='product_item')
]
