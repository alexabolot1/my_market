from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from basketapp.models import Basket


@login_required
def index(request):
    pass


@login_required
def basket_add(request, product_pk):
    basket_item, _ = Basket.objects.get_or_create(user=request.user,
                                                  product_id=product_pk)
    basket_item.quantity += 1
    basket_item.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def remove(request, pk):
    pass
