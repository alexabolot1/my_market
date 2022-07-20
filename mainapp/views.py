import random

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def get_category_menu():
    return Category.objects.filter(is_active=True)


def get_product_active_category():
    return Product.objects.filter(category__is_active=True)


def get_hot_product():
    return random.choice(get_product_active_category())


def get_same_products(hot_product):
    return Product.objects.filter(category=hot_product.category,
                                  category__is_active=True).exclude(id=hot_product.id)[:3]


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
    hot_product = get_hot_product()
    context = {
        'title': 'Продукты',
        'hot_product': hot_product,
        'same_products': get_same_products(hot_product)
    }
    return render(request, 'mainapp/products.html', context)


def category(request, pk):
    if pk == 0:
        cat = {'pk': 0, 'name': 'все'}
        prod = get_product_active_category()
    else:
        cat = get_object_or_404(Category, pk=pk)
        prod = Product.objects.filter(category=cat)
    paginator = Paginator(prod, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'title': 'товары категории',
        'category': cat,
        'page_obj': page_obj,
    }
    return render(request, 'mainapp/category_products.html', context)


def product_item(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product,
               'title': product.name,
               }
    return render(request, 'mainapp/product_item.html', context)
