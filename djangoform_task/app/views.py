from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse

# Create your views here.
def insert_topic(request):
    ETDFO=TopicDjForm()
    d={'ETDFO':ETDFO}
    if request.method=='POST':
        TDFDO=TopicDjForm(request.POST)
        if TDFDO.is_valid():
            tn=TDFDO.cleaned_data['topic_name']
            TTO=Topic.objects.get_or_create(topic_name=tn)
            ETDFO=TopicDjForm()
            if TTO[1]:
                return HttpResponse('topic is created')
            else:
                return HttpResponse('topic is already exist')
        else:
            return HttpResponse('invalid data')
    return render(request,'insert_topic.html',d)