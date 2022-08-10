from django.contrib import auth
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView

from authapp.forms import UserLoginForm, UserCreateForm, UserUpdateForm, UserProfileUpdateForm
from authapp.models import CustomUser, CustomUserProfile


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
    """
    Получает пользователя по email, проверяет совпадает ли код авторизации из ссылки
    с user_activation_key пользователя и не истекло ли время для авторизации
    """
    user = get_user_model().objects.filter(email=email).first()
    if user.user_activation_key == user_activation_key and not user.is_activation_key_expires:
        user.is_active = True
        user.save()
        auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
    return render(request, 'authapp/verification.html')


def update(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES,
                              instance=request.user)
        profile_form = UserProfileUpdateForm(request.POST, request.FILES,
                                             instance=request.user.customuserprofile)
        if form.is_valid() and profile_form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mainapp:index'))
    else:
        form = UserUpdateForm(instance=request.user)
        profile_form = UserProfileUpdateForm(instance=request.user.customuserprofile)

    context = {
        'page_title': 'редактирование',
        'form': form,
        'profile_form': profile_form,
    }
    return render(request, 'authapp/update.html', context)


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        CustomUserProfile.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.customuserprofile.save()
