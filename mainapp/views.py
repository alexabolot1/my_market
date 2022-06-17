from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def index(request):
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
    list_categories = Category.objects.filter(is_active=True)

    context = {
        'title': title,
        'products ': list_products,
        'categories': list_categories
    }
    return render(request, 'mainapp/products.html', context)


def category(request, pk):
    if pk == 0:
        cat = {'pk': 0, 'name': 'все'}
        prod = Product.objects.all()
    else:
        cat = get_object_or_404(Category, pk=pk)
        prod = Product.objects.filter(category=cat)
    context = {
        'title': 'товары категории',
        'categories': Category.objects.all(),
        'category': cat,
        'products': prod,
    }
    return render(request, 'mainapp/category_products.html', context)
