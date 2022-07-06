from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
# Create your views here.
from adminapp.forms import AdminUserUpdateForm, AdminUserCreateForm, CategoryCreateForm
from adminapp.mixin import DataMixin, SuperUserOnlyMixin, DeleteObjectMixin
from authapp.models import CustomUser
from mainapp.models import Category


# CRUD для пользователей
class CustomUserAdminRead(SuperUserOnlyMixin, DataMixin, ListView):
    model = CustomUser
    title = 'Админка|Пользователи'


class CustomUserAdminCreate(SuperUserOnlyMixin, DataMixin, CreateView):
    model = CustomUser
    form_class = AdminUserCreateForm
    success_url = reverse_lazy('adminapp:users_read')
    template_name = 'adminapp/user_create_update.html'
    title = 'Админка|Создание пользователя'


class CustomUserAdminUpdate(SuperUserOnlyMixin, DataMixin, UpdateView):
    model = CustomUser
    form_class = AdminUserUpdateForm
    success_url = reverse_lazy('adminapp:users_read')
    template_name = 'adminapp/user_create_update.html'
    title = 'Админка|Редактирование пользователя'


class CustomUserAdminDelete(SuperUserOnlyMixin, DataMixin, DeleteObjectMixin, DeleteView):
    model = CustomUser
    success_url = reverse_lazy('adminapp:users_read')
    title = 'Админка|Удаление пользотваеля'


# CRUD для категорий
class CategoryRead(SuperUserOnlyMixin, DataMixin, ListView):
    model = Category
    title = 'Админка|Категории'


class CategoryCreate(SuperUserOnlyMixin, DataMixin, CreateView):
    model = Category
    form_class = CategoryCreateForm
    success_url = reverse_lazy('adminapp:categories_read')
    title = 'Админка|Создание категории'


class CategoryUpdate(SuperUserOnlyMixin, DataMixin, UpdateView):
    model = Category
    form_class = CategoryCreateForm
    success_url = reverse_lazy('adminapp:categories_read')
    title = 'Админка|Редактирование категории'


class CategoryDelete(SuperUserOnlyMixin, DataMixin, DeleteObjectMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('adminapp:categories_read')
    title = 'Админка|Удаление категории'
