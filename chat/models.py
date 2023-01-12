from django.db import models
from datetime import date, datetime

# Create your models here.
class Room(models.Model):
  name = models.CharField(max_length=100)

class Messages(models.Model):
    value = models.CharField(max_length=100000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=20)
    room= models.CharField(max_length=25)
