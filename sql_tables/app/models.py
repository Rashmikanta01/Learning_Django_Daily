from django.db import models

# Create your models here.
class DEPT(models.Model):
    DEPTNO = models.IntegerField(primary_key=True)
    DNAME = models.CharField(max_length=50)
    LOC = models.CharField(max_length=50)
    def __str__(self):
        # return self.DNAME
        return str(self.DEPTNO)  #to return deptno as output
        
class EMP(models.Model):
    EMPNO = models.IntegerField(primary_key=True)
    ENAME = models.CharField(max_length=100)
    JOB = models.CharField(max_length=50)
    MGR = models.ForeignKey('self',on_delete=models.SET_NULL,null=True, blank=True)
    HIREDATE = models.DateField()
    SAL = models.DecimalField(max_digits=5,decimal_places=2)
    COMM = models.DecimalField(max_digits=5,decimal_places=2, null=True, blank=True)
    DEPTNO = models.ForeignKey(DEPT, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.EMPNO)
        #return self.ENAME #here we can comment this to return deptno as output

class BONUS(models.Model):
    ENAME = models.CharField(max_length=100)
    JOB = models.CharField(max_length=100)
    SAL = models.DecimalField(max_digits=5,decimal_places=2)
    COMM = models.DecimalField(max_digits=5,decimal_places=2)
    

class SALGRADE(models.Model):
    GRADE = models.IntegerField()
    LOSAL = models.IntegerField()
    HISAL = models.IntegerField()