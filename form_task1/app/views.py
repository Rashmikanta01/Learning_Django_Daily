from django.http import HttpResponse
from django.shortcuts import render

from app.models import *


# Create your views here.
def insert_topic(request):
    if request.method == 'POST':
        tn = request.POST['tn']
        TTO=Topic.objects.get_or_create(topic_name=tn)
        if TTO[1]:
            QLTO=Topic.objects.all()
            d={'QLTO': QLTO }
            return render(request,'display_topic.html' ,d)
        else:
            return HttpResponse('topic already exists') 
    return render(request, 'insert_topic.html')

def display_topic(request):
    QLTO=Topic.objects.all()
    d={'QLTO': QLTO }
    return render(request,'display_topic.html' ,d)


def insert_webpage(request):
    QLTO=Topic.objects.all()
    d={'QLTO': QLTO }
    if request.method == 'POST':
        tn=request.POST['tn']
        na=request.POST['na']
        ur=request.POST['ur']
        TTO=Topic.objects.get(topic_name=tn)
        WWO=WebPage.objects.get_or_create(topic_name=TTO,name=na,url=ur)
        if WWO[1]:
            return HttpResponse('webpage inserted successfully')
        else:
            return HttpResponse('webpage already exists')
    return render(request,'insert_webpage.html',d)

def insert_accessrecord(request):
    QLWO=WebPage.objects.all()
    d={'QLWO': QLWO ,
       }
    if request.method == 'POST':
        na=request.POST['na']
        au=request.POST['au']
        da=request.POST['da']
        WWO=WebPage.objects.get(name=na)
        ARO=AccessRecord.objects.get_or_create(name=WWO,author=au,date=da)
        if ARO[1]:
            return HttpResponse('accessrecord inserted successfully')
        else:
            return HttpResponse('accessrecord already exists')
    return render(request,'insert_accessrecord.html',d)

