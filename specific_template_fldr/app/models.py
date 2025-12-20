from django.db import models

# Create your models here.
class school(models.Model):
    name=models.CharField(max_length=250)
    addr=models.CharField(max_length=250)
    principal=models.CharField(max_length=250)
    def __str__(self):
        return self.name
    


class student(models.Model):
    name=models.CharField(max_length=250)
    age=models.IntegerField()
    school=models.ForeignKey(school,on_delete=models.CASCADE, related_name='students')
    def __str__(self):
        return self.name