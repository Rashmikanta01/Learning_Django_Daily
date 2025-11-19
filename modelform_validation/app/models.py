from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=15, validators=[RegexValidator(regex='[6-9]\d{9}')])