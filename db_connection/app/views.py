from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app.models import*

def insert_topic(request):
    tn=input('enter topic name')
    Tto=Topic.objects.get_or_create(topic_name=tn)
    if Tto[1]:
        return HttpResponse('Topic name is inserted')
    else:
        return HttpResponse('Topic is already present')
    
def insert_webpage(request):
    tn=input('enter topic name')
    Lto=Topic.objects.filter(topic_name=tn)

    if Lto:
        To=Lto[0]
        name=input('enter a name for webpage')
        url=input('enter a url')
        TWo=WebPage.objects.get_or_create(topic_name=To,name=name,url=url)

        if TWo[1]:
            return HttpResponse('one row is created in webpage')
        else:
            return HttpResponse('Given input is already present')
    else:
        return HttpResponse('Given Topic name is not present in Topic Table')
    
def insert_accesssrecord(request):
    Wid=int(input('webpageid'))
    LWo=WebPage.objects.get(id=Wid)
    if LWo:
        Wo=LWo[0]
        author=input('enter name of author')
        date=input('enter date in this fromat yyyy-mm-dd')
        TARO=AccessRecord.objects.get_or_create(name=Wo,author=author,date=date)
        if TARO[1]:
            return HttpResponse('one row is created in accessrecord')
        else:
            return HttpResponse('Given input is already present')
    else:
        return HttpResponse('Given webpage name is not present in webpage Table')
    