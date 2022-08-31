from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('', views.users_list),
    path('register_user', views.user_register)
]

