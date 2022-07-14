from django.contrib import auth
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
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
                return HttpResponseRedirect(reverse('mainapp:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'авторизация',
        'form': form,
    }
    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('mainapp:index'))


def register(request):
    if request.method == 'POST':
        user_form = UserCreateForm(request.POST, request.FILES)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.is_active = False
            user.set_activation_key()
            user.save()
            if not user.send_confirm_email():
                return HttpResponseRedirect(reverse('authapp:register'))
            return HttpResponseRedirect(reverse('mainapp:index'))
    else:
        user_form = UserCreateForm()

    context = {
        'title': 'регистрация',
        'form': user_form,
    }
    return render(request, 'authapp/register.html', context)


def verify(request, email, user_activation_key):
    user = get_user_model().objects.filter(email=email).first()
    if user.user_activation_key == user_activation_key and not user.is_activation_key_expires:
        user.is_active = True
        user.save()
        auth.login(request, user)
    return render(request, 'authapp/verification.html')


class UserUpdate(UpdateView):
    form_class = UserUpdateForm
    model = CustomUser
    success_url = reverse_lazy('mainapp:index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'редактирование пользователя'
        return context
