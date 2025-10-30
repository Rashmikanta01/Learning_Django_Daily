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
