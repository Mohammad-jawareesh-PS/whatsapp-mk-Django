from django.urls import path
from . import views

app_name = 'message_engine'

urlpatterns = [
  path('<slug:id>', views.message_engine, name='message_engine'),
]