from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.forms import *
def stdjform(request):
    SDF=StudentDjForm()
    d={'SDF':SDF}
    if request.method=='POST':
        SDF=StudentDjForm(request.POST)
        if SDF.is_valid():
            return HttpResponse(str(SDF.cleaned_data))
        else:
            return HttpResponse('invalid data')
    return render(request,'stdjform.html',d)

