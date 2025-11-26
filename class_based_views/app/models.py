from django.db import models

# Create your models here.

class school(models.Model):
    name = models.CharField(max_length=100)
    addr = models.CharField(max_length=100)
    pin = models.IntegerField()
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)