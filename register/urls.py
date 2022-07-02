from django.urls import path
from . import views

app_name = 'register'

urlpatterns = [
  path('login', views.Login, name='register.Login'),
  path('sign-up', views.Sign_up, name='register.Sign_up'),
]