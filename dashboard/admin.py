from django.contrib import admin
from .models import Tasks, Sent_Numbers, Received_Numbers, Message, User_config

# Register your models here.

admin.site.register(Tasks)
admin.site.register(Sent_Numbers)
admin.site.register(Received_Numbers)
admin.site.register(Message)
admin.site.register(User_config)