from django.urls import path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('users/read/', adminapp.user_read, name='user_read'),
    path('user/update/<int:user_pk>', adminapp.user_update, name='user_update'),
    path('user/create/', adminapp.user_create, name='user_create'),
    path('user/delete/<int:user_pk>', adminapp.user_delete, name='user_delete'),
]
