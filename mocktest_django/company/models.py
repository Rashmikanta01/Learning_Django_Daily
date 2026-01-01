from django.db import models

# Create your models here.
from django.db import models

class Company(models.Model):
    id = models.BigAutoField(primary_key=True)
    company_name = models.CharField(max_length=255,null=False,blank=False)
    email_id = models.EmailField(unique=False,null=False,blank=False)
    company_code = models.CharField(max_length=5,unique=True,null=True,blank=True)
    strength = models.IntegerField(null=True,blank=True)
    website = models.URLField(null=True,blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.company_name
