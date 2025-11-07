from django.shortcuts import render

from app.forms import *
from django.http import HttpResponse

# Create your views here.
def insert_to_modelform(request):
    EMFO= TopicMF()
    d={'EMFO':EMFO}
    if request.method =='POST':
        TMFO=TopicMF(request.POST)
        if TMFO.is_valid():
            TMFO.save()
            return HttpResponse('created')
        else:
            return HttpResponse('invalid')



    return render(request,'insert_to_modelform.html',d)

def insert_webpageMF(request):
    EWMFO= WebpageMF()
    d={'EWMFO': EWMFO}
    if request.method == 'POST':
        WTMFO = WebpageMF(request.POST)
        if WTMFO.is_valid():
            WTMFO.save()
            return HttpResponse('created')
        else:
            return HttpResponse('invalid')

    return render(request, 'insert_webpageMF.html', d)

def insert_accessMF(request):
    EAMFO = AccessMF()
    d = {'EAMFO': EAMFO}
    if request.method == 'POST':
        WAMFO = AccessMF(request.POST)
        if WAMFO.is_valid():
            WAMFO.save()
            return HttpResponse('created')
        else:
            return HttpResponse('invalid')

    return render(request, 'insert_accessMF.html', d)

def insert_countriesMF(request):
    ECOMFO = CountriesMF()
    d = {'ECOMFO': ECOMFO}
    if request.method == 'POST':
        COMFO = CountriesMF(request.POST)
        if COMFO.is_valid():
            COMFO.save()
            return HttpResponse('created')
        else:
            return HttpResponse('invalid')

    return render(request, 'insert_countriesMF.html', d)

