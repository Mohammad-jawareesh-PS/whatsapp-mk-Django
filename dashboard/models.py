from django.db import models
from register.models import Profile
from offers.models import Monthly_offers, Normal_offers

# Create your models here.

class Tasks(models.Model):
  user = models.ForeignKey(Profile, on_delete=models.CASCADE)
  name = models.CharField(max_length=50)
  phone_number = models.CharField(max_length=50)
  country = models.CharField(max_length=50)
  ranges = models.IntegerField()
  message = models.TextField(max_length=1000)
  available = models.BooleanField(default=True)
  date_work = models.IntegerField(default=0)
  added_date = models.DateTimeField(auto_now=True)


  def __str__(self):
    return self.name



class Sent_Numbers(models.Model):
  name = models.CharField(max_length=50)
  phone_number = models.CharField(max_length=50)
  country = models.CharField(max_length=50)
  available = models.BooleanField(default=True)
  
  def __str__(self):
    return self.phone_number



class Received_Numbers(models.Model):
  name = models.CharField(max_length=50)
  phone_number = models.CharField(max_length=50)
  country = models.CharField(max_length=50)

  def __str__(self):
    return self.phone_number



class Message(models.Model):
  user = models.ForeignKey(Profile, on_delete=models.CASCADE)
  task = models.ForeignKey(Tasks, related_name='+', on_delete=models.CASCADE)
  received_number = models.ForeignKey(Received_Numbers, on_delete=models.CASCADE)
  sent_number = models.CharField(max_length=50)
  message = models.TextField(max_length=1000)
  date_send = models.IntegerField(default=0)
  added_date = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.message



class User_config(models.Model):
  user = models.ForeignKey(Profile, on_delete=models.CASCADE)
  monthly_offers = models.ForeignKey(Monthly_offers, on_delete=models.CASCADE, null=True, blank=True)
  normal_offers = models.ForeignKey(Normal_offers, on_delete=models.CASCADE, null=True, blank=True)
  total_received_numbers = models.IntegerField(default=0)
  sent_number_type = models.CharField(max_length=20, default="shared")
  daily_operations = models.IntegerField(default=2)
  day_use =  models.IntegerField(default=0)

  def __str__(self):
    return str(self.user)