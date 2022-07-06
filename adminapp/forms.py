from django.contrib.auth import get_user_model
from django.forms import ModelForm

from authapp.forms import UserUpdateForm, UserCreateForm
from mainapp.models import Category, Product


class AdminUserUpdateForm(UserUpdateForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'password',
                  'email', 'age', 'avatar',
                  'is_staff', 'is_superuser', 'is_active')


class AdminUserCreateForm(UserCreateForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name',
                  'password1', 'password2', 'email', 'age', 'avatar',
                  'is_staff', 'is_superuser', 'is_active')


class AdminCategoryCreateForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control {field_name}'


class AdminProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control {field_name}'
