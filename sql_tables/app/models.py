from django.db import models

# Create your models here.
class DEPT(models.Model):
    DEPTNO = models.IntegerField(primary_key=True)
    DNAME = models.CharField(max_length=50)
    LOC = models.CharField(max_length=50)

class EMP(models.Model):
    EMPNO = models.IntegerField(primary_key=True)
    ENAME = models.CharField(max_length=100)
    JOB = models.CharField(max_length=50)
    MGR = models.ForeignKey('self',on_delete=models.SET_NULL,null=True, blank=True)
    HIREDATE = models.DateField()
    SAL = models.DecimalField(max_digits=5,decimal_places=5)
    COMM = models.DecimalField(max_digits=5,decimal_places=5, null=True, blank=True)
    DEPTNO = models.ForeignKey(DEPT, on_delete=models.CASCADE)

class BONUS(models.Model):
    ENAME = models.CharField(max_length=100)
    JOB = models.CharField(max_length=100)
    SAL = models.DecimalField(max_digits=5,decimal_places=5)
    COMM = models.DecimalField(max_digits=5,decimal_places=5)

class SALGRADE(models.Model):
    GRADE = models.IntegerField()
    LOSAL = models.IntegerField()
    HISAL = models.IntegerField()