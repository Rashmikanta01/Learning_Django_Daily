from django.shortcuts import render
import datetime
# Create your views here.
def filters(request):
    d={'data':'hello world','count':5,}
    

    return render(request, 'filters.html',d)