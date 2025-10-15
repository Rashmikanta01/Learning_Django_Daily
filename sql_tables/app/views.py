from django.shortcuts import render

# Create your views here.
from app.models import *

def emptodeptjoin(request):
    QLEDO=EMP.objects.all().select_related('DEPTNO')
    d={'QLEDO': QLEDO }
    return render(request,'emptodeptjoin.html' ,d)