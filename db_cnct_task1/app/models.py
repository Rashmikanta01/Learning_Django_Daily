from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Countries(models.Model):
    countries_id=models.IntegerField(primary_key=True)
    Countries_name=models.CharField(max_length=100)
    def __str__(self):
        return self.Countries_name
class Capitals(models.Model):
    Countries_id=models.OneToOneField(Countries,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)

