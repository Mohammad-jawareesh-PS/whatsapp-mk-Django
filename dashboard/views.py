from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
# import webbrowser as web
# import pyautogui as pg
import time
import datetime

from register.models import Profile
from .models import Tasks, Sent_Numbers, Received_Numbers, Message, User_config

from selenium_conf.automation import ChromeBrowser

# dashboard
@login_required(login_url='/register/login')
def dashboard(request):
  today = datetime.datetime.today()
  profile = Profile.objects.get(user=request.user)
  tasks = Tasks.objects.filter(user=profile).order_by('-added_date')
  user_config = User_config.objects.get(user=profile)

  tasks_len = len(tasks)
  available_tasks_len = len(Tasks.objects.filter(user=profile, available=True))

  for task in tasks:
    if task.date_work != today.day:
      task.available = True
      task.save()

  if user_config.day_use != today.day:
    if user_config.monthly_offers:
      user_config.daily_operations = user_config.monthly_offers.daily_operations
      user_config.save()






  context = {
    # basic 
    'title': 'Dashboard',
    'description': '',
    'css': ['dashboard/main.css'],
    'js': ['dashboard/main.js'],
    
    'profile': profile,
    'tasks': tasks,
    'user_config': user_config,
    'tasks_len': tasks_len,
    'available_tasks_len': available_tasks_len,
    'total_messages': len(Message.objects.filter(user=profile)),
    'todat_messages': len(Message.objects.filter(user=profile, date_send=today.day)),
    
  }

  if Sent_Numbers.objects.filter(available=True).exists():
    context.update({'sent_number_available': True,})


  if user_config.daily_operations != 0:
    context.update({'daily_operations': True,})


  if user_config.total_received_numbers != 0:
    context.update({'total_received_numbers': True,})



  if request.GET.get('task_name') and request.GET.get('message') and request.GET.get('range'):
    # phone_number = request.GET.get('user_phone_number')
    phone_number = user_config.monthly_offers.sent_number_type
    task_name = request.GET.get('task_name')
    message = request.GET.get('message')
    ranges = request.GET.get('range')
    date_work = today.day
    # country = request.GET.get('country')

    
    Tasks(user=profile, name=task_name, phone_number=phone_number, country='', ranges=ranges, message=message, date_work=date_work).save()

    return redirect('/dashboard')



  if request.GET.get('start'):
    statu = str(request.GET.get('start')).split(',')[0]
    task_id = str(request.GET.get('start')).split(',')[1]
    task = Tasks.objects.get(id=int(task_id), user=profile)

    if statu == 'delet' and task_id:
      task.delete()
      return redirect('/dashboard')

    elif statu == 'start' and task_id:
      task.available = False
      task.save()
    
      user_config.total_received_numbers -= task.ranges
      user_config.daily_operations -= 1
      user_config.day_use = today.day
      user_config.save()



      sent_numbers = Sent_Numbers.objects.all()
      received_numbers = Received_Numbers.objects.all()

      for sent_number in sent_numbers[:task.ranges]:
        print(task.ranges)
        print(type(task.ranges))
        print('#')
        if sent_number.available == True:
          this_sent_number = Sent_Numbers.objects.get(phone_number=sent_number)
          this_sent_number.available = False
          this_sent_number.save()
          for received_number in received_numbers:
            try:
              ChromeBrowser(sent_number, received_number, task.message)
            except:
              this_sent_number.available = True
              this_sent_number.save()
              break

            Message(
              user=profile,
              task=task,
              received_number=Received_Numbers.objects.filter(phone_number=received_number)[0],
              sent_number=sent_number,
              message=task.message,
              date_send= today.day,
            ).save()
          
          this_sent_number.available = True
          this_sent_number.save()
          break
      return redirect('/dashboard')

  if request.GET.get('logout') == 'True':
    logout(request)
    return redirect('/register/login')




  return render(request, 'dashboard.html', context)

