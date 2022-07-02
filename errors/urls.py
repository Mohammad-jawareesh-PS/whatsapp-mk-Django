from django.urls import path
from . import views

app_name = 'errors'

urlpatterns = [
  # path('/monthly', views.monthly_offers, name='offers'),
  path('', views.start, name='start'),
]