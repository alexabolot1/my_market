from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
# Create your views here.
from adminapp.forms import AdminUserUpdateForm, AdminUserCreateForm, AdminCategoryCreateForm, AdminProductForm
from adminapp.mixin import DataMixin, SuperUserOnlyMixin, DeleteObjectMixin
from authapp.models import CustomUser
from mainapp.models import Category, Product


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
class CategoryAdminRead(SuperUserOnlyMixin, DataMixin, ListView):
    model = Category
    title = 'Админка|Категории'


class CategoryAdminCreate(SuperUserOnlyMixin, DataMixin, CreateView):
    model = Category
    form_class = AdminCategoryCreateForm
    success_url = reverse_lazy('adminapp:categories_read')
    title = 'Админка|Создание категории'


class CategoryAdminUpdate(SuperUserOnlyMixin, DataMixin, UpdateView):
    model = Category
    form_class = AdminCategoryCreateForm
    success_url = reverse_lazy('adminapp:categories_read')
    title = 'Админка|Редактирование категории'


class CategoryAdminDelete(SuperUserOnlyMixin, DataMixin, DeleteObjectMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('adminapp:categories_read')
    title = 'Админка|Удаление категории'


# CRUD для продуктов
class ProductAdminRead(SuperUserOnlyMixin, DataMixin, ListView):
    model = Product
    title = 'Админка|Продукты'


class ProductAdminCreate(SuperUserOnlyMixin, DataMixin, CreateView):
    model = Product
    form_class = AdminProductForm
    success_url = reverse_lazy('adminapp:products_read')
    title = 'Админка|Создание продукта'


class ProductAdminUpdate(SuperUserOnlyMixin, DataMixin, UpdateView):
    model = Product
    form_class = AdminProductForm
    success_url = reverse_lazy('adminapp:products_read')
    title = 'Админка|Редактирование продукта'


class ProductAdminDelete(SuperUserOnlyMixin, DataMixin, DeleteObjectMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('adminapp:products_read')
    title = 'Админка|Удаление продукта'


class ProductAdminDetail(SuperUserOnlyMixin, DataMixin, DetailView):
    model = Product
    title = 'Админка|Продукт'