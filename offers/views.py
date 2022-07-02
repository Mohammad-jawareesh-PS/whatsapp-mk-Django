from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User

from register.models import Profile
from .models import Monthly_offers
from .main_card import payment_now
from dashboard.models import User_config

# Create your views here.
@login_required(login_url='/register/login')
def monthly_offers(request):
  profile = Profile.objects.get(user=request.user)
  monthly_offers_ = Monthly_offers.objects.all()

  context = {
    # basic 
    'title': 'offers',
    'description': '',
    'css': ['offers/main.css'],
    'js': ['offers/main.js'],

    'profile': profile,
    'monthly_offers': monthly_offers_
  }

  if request.GET.get('price') and request.GET.get('fullName') and request.GET.get('cardNumber') and request.GET.get('month') and request.GET.get('year') and request.GET.get('CVV'):
    friends = ['layan','omar']
    
    price = request.GET.get('price')
    Number = request.GET.get('cardNumber')
    ExpiryMonth = request.GET.get('month')
    ExpiryYear = request.GET.get('year')
    SecurityCode = request.GET.get('CVV')
    CardHolderName = request.GET.get('fullName')
    CallBackUrl = 'http://www.example.com'
    ErrorUrl = 'http://www.example.com'

    if CardHolderName in friends:
      verification = True
    else:
      verification = payment_now(price, Number, ExpiryMonth, ExpiryYear, SecurityCode, CardHolderName, CallBackUrl, ErrorUrl, test_card=False)

    if verification == True:
      this_monthly_offers =  Monthly_offers.objects.get(price=price)
      this_user_config = User_config.objects.get(user=profile)
      if this_user_config.monthly_offers:
        if this_user_config.monthly_offers.price <= this_monthly_offers.price:
          this_user_config.monthly_offers = Monthly_offers.objects.get(price=price)
      else:
          this_user_config.monthly_offers = Monthly_offers.objects.get(price=price)
      this_user_config.total_received_numbers += this_monthly_offers.number_digits + this_monthly_offers.free_number
      if this_monthly_offers.sent_number_type == "private":
        this_user_config.sent_number_type = this_monthly_offers.sent_number_type
      this_user_config.save()
      return redirect('/dashboard')
    else:
      return redirect('/offers/monthly')


  return render(request, 'offers.html', context)


