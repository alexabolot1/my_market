from django.shortcuts import render
from .models import Product, Category


def index(request):
    context = {
        'title': 'My_market'
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    title = 'Продукты'
    list_products = Product.objects.filter(is_active=True)

    context = {
        'title': title,
        'list_products ': list_products
    }

    return render(request, 'mainapp/products.html', context)
