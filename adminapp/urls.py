from django.urls import path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.CustomUserAdminRead.as_view(), name='users_read'),
    path('user/update/<int:pk>/', adminapp.CustomUserAdminUpdate.as_view(), name='user_update'),
    path('user/create/', adminapp.CustomUserAdminCreate.as_view(), name='user_create'),
    path('user/delete/<int:pk>/', adminapp.CustomUserAdminDelete.as_view(), name='user_delete'),

    path('categories/', adminapp.CategoryRead.as_view(), name='categories_read'),
    path('category/create/', adminapp.CategoryCreate.as_view(), name='category_create'),
    path('category/update/<int:pk>/', adminapp.CategoryUpdate.as_view(), name='category_update')
]
