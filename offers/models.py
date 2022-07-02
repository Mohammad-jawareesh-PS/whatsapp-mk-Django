from django.db import models

# Create your models here.




class Monthly_offers(models.Model):
  price = models.DecimalField(max_digits=10,  decimal_places=2)
  number_digits = models.IntegerField()
  free_number = models.IntegerField(default=0)
  number_of_daily_operations = models.IntegerField(default=100)
  daily_operations = models.IntegerField(default=2)
  sent_number_type = models.CharField(choices=[('shared', 'shared'), ('private','private')], max_length=50, default='shared')
  message_type = models.CharField(choices=[('text', 'text')], max_length=50, default='text')

  def __str__(self):
    return f'${self.price}'


class Normal_offers(models.Model):
  price = models.DecimalField(max_digits=10,  decimal_places=2)
  number_digits = models.IntegerField()
  free_number = models.IntegerField(default=0)
  number_of_daily_operations = models.IntegerField(default=100)
  daily_operations = models.IntegerField(default=2)
  sent_number_type = models.CharField(choices=[('shared', 'shared'), ('private','private')], max_length=50, default='shared')
  message_type = models.CharField(choices=[('text', 'text')], max_length=50, default='text')

  def __str__(self):
    return f'${self.price}'