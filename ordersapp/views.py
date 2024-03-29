from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from ordersapp.forms import OrderForm, OrderItemForm
from ordersapp.models import Order, OrderItem


class OrderList(ListView):
    model = Order

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class OrderCreate(CreateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('ordersapp:order_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        OrderFormSet = inlineformset_factory(Order, OrderItem, form=OrderItemForm, extra=3)
        if self.request.POST:
            formset = OrderFormSet(self.request.POST, self.request.FILES)
        else:
            basket_items = self.request.user.basket.all()
            context['form'].initial['user'] = self.request.user
            if basket_items and basket_items.count():
                OrderFormSet = inlineformset_factory(Order, OrderItem, form=OrderItemForm,
                                                     extra=basket_items.count() + 1)
                formset = OrderFormSet()
                for form, basket_item in zip(formset.forms, basket_items):
                    form.initial['product'] = basket_item.product
                    form.initial['quantity'] = basket_item.quantity
            else:
                formset = OrderFormSet()
        context['orderitems'] = formset
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        orderitems = context['orderitems']

        with transaction.atomic():
            order = super().form_valid(form)
            if orderitems.is_valid():
                orderitems.instance = self.object  # one to many
                orderitems.save()
                self.request.user.basket.all().delete()
        if self.object.total_cost == 0:
            self.object.delete()
        return order


class OrderUpdate(UpdateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('ordersapp:order_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        OrderFormSet = inlineformset_factory(Order,
                                             OrderItem,
                                             form=OrderItemForm,
                                             extra=1)
        if self.request.POST:
            formset = OrderFormSet(self.request.POST,
                                   self.request.FILES,
                                   instance=self.object)
        else:
            formset = OrderFormSet(instance=self.object)
            for form in formset.forms:
                instance = form.instance
                if instance.pk:
                    form.initial['price'] = instance.product.price
        context['orderitems'] = formset
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        orderitems = context['orderitems']
        with transaction.atomic():
            order = super().form_valid(form)
            if orderitems.is_valid():
                orderitems.save()
            else:
                print(vars(orderitems))
        # удаляю пустой заказ
        if self.object.total_cost == 0:
            self.object.delete()
        return order


class OrderDetail(DetailView):
    model = Order


class OrderDelete(DeleteView):
    model = Order
    success_url = reverse_lazy('ordersapp:order_list')
