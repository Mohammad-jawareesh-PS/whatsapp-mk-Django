from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Profile
from dashboard.models import User_config
from register.models import Profile

# Create your views here.


# login
def Login(request):
  if not request.user.is_authenticated:
    context = {}

    if request.GET.get('username') and request.GET.get('password'):
      username = request.GET.get('username')
      password = request.GET.get('password')
      print(username)
      print(password)
      user = authenticate(username=username, password=password)
      if user:
        login(request, user)
        return redirect('/dashboard')
      else:
        return redirect('/register/login')

    return render(request, 'login.html', context)
  else :
    return redirect('/dashboard')
  


# sign_up
def Sign_up(request):
  if not request.user.is_authenticated:
    context = {}

    if request.GET.get('username') and request.GET.get('email') and request.GET.get('password'):
      username = request.GET.get('username')
      email = request.GET.get('email')
      password = request.GET.get('password')
      user = authenticate(username=username, password=password)
      if user:
        login(request, user)
        return redirect('/dashboard')
      else:
        if not User.objects.filter(username=username).exists() and not User.objects.filter(email=email).exists():
          user = User.objects.create_user(username, email, password)
          Profile(user=user).save()
          login(request, user)
          profile = Profile.objects.get(user=user)
          User_config(user=profile).save()
          return redirect('/dashboard')
        else:
          return redirect('/register/sign-up')

    return render(request, 'sign_up.html', context)
  else:
    return redirect('/dashboard')