from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.forms import *
def stdjform(request):
    SDF=StudentDjForm()
    d={'SDF':SDF}
    if request.method=='POST':
        SFDO=StudentDjForm(request.POST)
        if SFDO.is_valid():
            return HttpResponse(str(SFDO.cleaned_data))
        else:
            return HttpResponse('invalid data')
    return render(request,'stdjform.html',d)

