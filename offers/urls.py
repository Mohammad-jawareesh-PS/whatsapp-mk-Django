from django.urls import path
from . import views

app_name = 'offers'

urlpatterns = [
  # path('/monthly', views.monthly_offers, name='offers'),
  path('/normal', views.monthly_offers, name='offers'),
]