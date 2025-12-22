from django.db import models

# Create your models here.
class School(models.Model):
    scname=models.CharField(max_length=100)
    scaddr=models.CharField(max_length=100)
    schead=models.CharField(max_length=100)

