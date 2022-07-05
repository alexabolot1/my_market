from django.contrib import auth
from django.forms import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView

from authapp.forms import UserLoginForm, UserCreateForm, UserUpdateForm
from authapp.models import CustomUser


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'авторизация',
        'form': form,
    }
    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))


def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        form = UserCreateForm()

    context = {
        'title': 'регистрация',
        'form': form,
    }
    return render(request, 'authapp/register.html', context)


class UserUpdate(UpdateView):
    form_class = UserUpdateForm
    model = CustomUser
    success_url = reverse_lazy('mainapp:index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'редактирование пользователя'
        return context
