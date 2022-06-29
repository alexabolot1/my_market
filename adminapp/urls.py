from django.urls import path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('users/read/', adminapp.user_read, name='user_read'),
]
