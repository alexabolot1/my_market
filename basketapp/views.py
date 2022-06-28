from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.template.loader import render_to_string

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
def basket_remove(request, basket_item_pk):
    item = get_object_or_404(BasketItem, pk=basket_item_pk)
    item.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_update(request, basket_item_pk, basket_item_quantity):
    if request.is_ajax:
        new_basket_item = BasketItem.objects.filter(pk=basket_item_pk).first()
        if not new_basket_item:
            return JsonResponse({'status': False})
        if basket_item_quantity > 0:
            new_basket_item.quantity = basket_item_quantity
            new_basket_item.save()
        else:
            new_basket_item.delete()
        basket_summary_html = render_to_string('basketapp/includes/basket_summary.html',
                                               request=request)
        return JsonResponse({'status': True,
                             'basket_summary': basket_summary_html})
