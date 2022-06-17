from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from basketapp.models import BasketItem


@login_required
def index(request):
    basket = request.user.basket.all()
    context = {
        'title': 'Корзина',
        'basket': basket,
    }
    return render(request, 'basketapp/index.html', context)


@login_required
def basket_add(request, product_pk):
    basket_item, _ = BasketItem.objects.get_or_create(user=request.user,
                                                  product_id=product_pk)
    basket_item.quantity += 1
    basket_item.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_remove(request, pk):
    BasketItem.objects.filter(pk=pk).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

