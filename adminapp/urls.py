from django.urls import path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.CustomUserAdminRead.as_view(), name='users_read'),
    path('user/update/<int:pk>/', adminapp.CustomUserAdminUpdate.as_view(), name='user_update'),
    path('user/create/', adminapp.CustomUserAdminCreate.as_view(), name='user_create'),
    path('user/delete/<int:pk>/', adminapp.CustomUserAdminDelete.as_view(), name='user_delete'),

    path('categories/', adminapp.CategoryAdminRead.as_view(), name='categories_read'),
    path('category/create/', adminapp.CategoryAdminCreate.as_view(), name='category_create'),
    path('category/update/<int:pk>/', adminapp.CategoryAdminUpdate.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', adminapp.CategoryAdminDelete.as_view(), name='category_delete'),

    path('products/', adminapp.ProductAdminRead.as_view(), name='products_read'),
    path('product/create/', adminapp.ProductAdminCreate.as_view(), name='product_create'),
    path('product/update/<int:pk>/', adminapp.ProductAdminUpdate.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', adminapp.ProductAdminDelete.as_view(), name='product_delete'),
    path('product/detail/<int:pk>/', adminapp.ProductAdminDetail.as_view(), name='product_detail'),
]
