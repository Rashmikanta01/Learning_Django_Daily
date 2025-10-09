from django.db import models

# Create your models here.

#creating a table for author books name ...

class Author(models.Model):
    Aid=models.IntegerField(primary_key=True)
    Aname=models.CharField(max_length=100)
    phone=models.IntegerField(unique=True)

class Books(models.Model):
    Aid=models.ForeignKey(Author,on_delete=models.CASCADE)
    Bid=models.IntegerField(primary_key=True)
    bname=models.CharField(max_length=100)
    Pbdate=models.DateField()