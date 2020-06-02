from django.db import models
import datetime
from django.utils import timezone


# Create your models here.

class Rate(models.Model):
    AHT = models.IntegerField(default=200)
    RP = models.IntegerField(default=60)
    SL = models.FloatField(default=0.8)
    TAT = models.IntegerField(default=60)
    Shrink = models.FloatField(default=0.2)
    Calls = models.IntegerField(default=50)

