from django.contrib.auth import get_user_model

from authapp.forms import UserUpdateForm, UserCreateForm


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
