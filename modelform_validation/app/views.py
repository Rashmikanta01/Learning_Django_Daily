from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *

# Create your views here.
def insert_student(request):
    ESMFO=StudentMF()
    d={'ESMFO':ESMFO}
    if request.method=='POST':
        SMFO=StudentMF(request.POST)
        if SMFO.is_valid():
            SMFO.save()
            return HttpResponse("Data Inserted Successfully")
        else:
            return HttpResponse("Invalid Data")
    return render(request,'insert_student.html',d)
