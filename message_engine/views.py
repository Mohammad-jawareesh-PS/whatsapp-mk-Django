from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
import time

from register.models import Profile
from dashboard.models import Tasks, Sent_Numbers, Received_Numbers, Message
from dashboard.models import User_config

# Create your views here.
@login_required(login_url='/register/login')
def message_engine(request, id):

  this_task = Tasks.objects.get(id=id)
  profile = Profile.objects.get(user=request.user)
  tasks = Tasks.objects.filter(user=profile)
  numbers = Received_Numbers.objects.all()
  messages = Message.objects.filter(user=profile)

  context = {
    # basic 
    'title': 'Message Engine',
    'description': '',
    'css': ['dashboard/main.css', 'message_engine/main.css'],
    'js': ['message_engine/main.js'],

    'profile': profile,
    'tasks': tasks,
    'numbers': numbers[:this_task.ranges],
    'messages': messages,
    'this_task': this_task,
  }
  

  return render(request, 'message_engine.html', context)