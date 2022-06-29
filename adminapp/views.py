from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse

from adminapp.forms import AdminUserUpdateForm, AdminUserCreateForm
from authapp.models import CustomUser


@user_passes_test(lambda user: user.is_superuser)
def user_read(request):
    all_users = CustomUser.objects.all()
    context = {'title': 'Админка | Все пользователи',
               'all_users': all_users}
    return render(request, 'adminapp/user_read.html', context)


def user_create(request):
    if request.method == 'POST':
        form = AdminUserCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:user_read'))
    else:
        form = AdminUserCreateForm()

    context = {'title': 'Админка | Создание пользователя',
               'form': form}
    return render(request, 'adminapp/user_update.html', context)


def user_update(request, user_pk):
    user = get_object_or_404(CustomUser, pk=user_pk)
    if request.method == 'POST':
        form = AdminUserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:user_read'))
    else:
        form = AdminUserUpdateForm(instance=user)
    context = {'title': 'Админка | Редактирование пользователя',
               'form': form}
    return render(request, 'adminapp/user_update.html', context)
