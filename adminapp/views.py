from django.shortcuts import render


# Create your views here.
from authapp.models import CustomUser


def user_read(request):
    all_users = CustomUser.objects.all()
    context = {'title': 'Админка | Все пользователи',
               'all_users': all_users}
    return render(request, 'adminapp/user_read.html', context)
