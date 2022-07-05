from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy

# Create your views here.
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from adminapp.forms import AdminUserUpdateForm, AdminUserCreateForm, CategoryCreateForm
from authapp.models import CustomUser
from mainapp.models import Category


# Представления для работы с пользователями
class CustomUserAdminRead(ListView):
    model = CustomUser


class CustomUserAdminCreate(CreateView):
    model = CustomUser
    form_class = AdminUserCreateForm
    success_url = reverse_lazy('adminapp:users_read')
    template_name = 'adminapp/user_create_update.html'


class CustomUserAdminUpdate(UpdateView):
    model = CustomUser
    form_class = AdminUserUpdateForm
    success_url = reverse_lazy('adminapp:users_read')
    template_name = 'adminapp/user_create_update.html'


class CustomUserAdminDelete(DeleteView):
    model = CustomUser
    success_url = reverse_lazy('adminapp:users_read')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_active:
            self.object.is_active = False
        else:
            self.object.is_active = True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


# @user_passes_test(lambda user: user.is_superuser)
# def user_delete(request, user_pk):
#     user = get_object_or_404(CustomUser, pk=user_pk)
#     if not user.is_active or request.method == 'POST':
#         if user.is_active:
#             user.is_active = False
#         else:
#             user.is_active = True
#         user.save()
#         return HttpResponseRedirect(reverse('adminapp:users_read'))
#     context = {'title': 'Админка | Удаление пользователя',
#                'user_to_delete': user}
#     return render(request, 'adminapp/user_delete.html', context)


# Представления для работы с категориями
class CategoryRead(ListView):
    model = Category


class CategoryCreate(CreateView):
    model = Category
    form_class = CategoryCreateForm
    success_url = reverse_lazy('adminapp:categories_read')


class CategoryUpdate(UpdateView):
    model = Category
    form_class = CategoryCreateForm
    success_url = reverse_lazy('adminapp:categories_read')
