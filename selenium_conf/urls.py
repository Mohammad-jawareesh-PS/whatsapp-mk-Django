from django.urls import path
from . import views

app_name = 'selenium_conf'

urlpatterns = [
  path('setting/add/sent-number', views.Add_sent_number, name='add_sent_number'),
  path('setting/add', views.Add, name='add_sent_number'),
]