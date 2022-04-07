from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def main(request):
    context = {
        'title': 'My_market'
    }
    return render(request, 'mainapp/index.html', context)

def contacts(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'mainapp/contacts.html', context)

def products(request):
    title = 'Продукты'
    list_products = Product.objects.filter(is_active=True)

    context = {
        'title': title,
        'list_products ': list_products
    }
    return render(request, 'mainapp/products.html', context)


def product(request, pk):
    product = Product.objects.get(pk=pk)

    title = f'{product.name}'

    context = {
        'title': title,
        'product': get_object_or_404(Product, pk=pk)
    }

    return render(request, 'mainapp/product_details.html', context)