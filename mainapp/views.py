from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def main(request):
    context = {
        'title': 'Магазин'
    }
    return render(request, 'mainapp/index.html', context)


def contacts(request):
    locations = [
        {'city': 'Москва',
        'phone': '+7-888-213-1234',
        'email': 'info.msk@mymarket.ru',
        'address': 'МКАД'},
        {'city': 'Екатеринбург',
         'phone': '+7-343-243-1232',
         'email': 'info.ekb@mymarket.ru',
         'address': 'Пионерский'},
        {'city': 'Санкт-Петербург',
         'phone': '+7-777-213-1253',
         'email': 'info.spb@mymarket.ru',
         'address': 'Купчино'},
    ]

    context = {
        'title': 'Контакты',
        'locations': locations
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


# def product(request, pk):
#     product_item = Product.objects.get(pk=pk)
#     title = f'{product_item.name}'
#     context = {
#         'title': title,
#         'product': get_object_or_404(Product, pk=pk)
#     }
#     return render(request, 'mainapp/product_details.html', context)
