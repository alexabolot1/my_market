from django.urls import path
import authapp.views as authapp

app_name = 'authapp'

urlpatterns = [
    path('login/', authapp.login, name='login'),
    path('logout/', authapp.logout, name='logout'),
    path('register/', authapp.register, name='register'),
    path('update/<int:pk>', authapp.UserUpdate.as_view(), name='update'),
    path('user/verify/<str:email>/<str:user_activation_key>/', authapp.verify, name='verify')
]
