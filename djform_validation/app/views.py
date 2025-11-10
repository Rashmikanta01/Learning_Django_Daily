from django.shortcuts import render

from django.http import HttpResponse
from app.forms import *
from app.models import *

# Create your views here.
def student_form_view(request):
    DSFO=StudentForm()
    d={'DSFO':DSFO}
    if request.method=='POST':
        SFO=StudentForm(request.POST)
        if SFO.is_valid():
            return HttpResponse(str(SFO.cleaned_data))
        else:
            return HttpResponse('invalid data')

    return render(request, 'student_form.html',d)
#superuser pass word 'y'