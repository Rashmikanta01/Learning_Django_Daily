from django.http import HttpResponse
from django.shortcuts import render
#from django.db. function import Length
# here we can insert the data into database
from app.models import*
from django.db.models import Q

def insert_topic(request):
    tn=input('enter topic name')
    Tto=Topic.objects.get_or_create(topic_name=tn)
    if Tto[1]:
         QLTO=Topic.objects.all()
         d={'QLTO': QLTO }
         return render(request,'display_topic.html' ,d)
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
            QLTO=Topic.objects.all()
            d={'QLTO': QLTO }
            return render(request,'display_topic.html' ,d)

        else:
            return HttpResponse('Given input is already present')
    else:
        return HttpResponse('Given Topic name is not present in Topic Table')
    
def insert_accesssrecord(request):
    Wid=int(input('webpageid'))
    LWo=WebPage.objects.filter(id=Wid)
    if LWo:
        Wo=LWo[0]
        author=input('enter name of author')
        date=input('enter date in this fromat yyyy-mm-dd')
        TARO=AccessRecord.objects.get_or_create(name=Wo,author=author,date=date)
        if TARO[1]:
            QLARO=AccessRecord.objects.all()
            d={'QLARO': QLARO }
            return render(request,'display_accessrecord.html' ,d)
        else:
            return HttpResponse('Given input already present')
    else:
        return HttpResponse('Given webpage name is not present in webpage Table')
    
#here we can display the data from database and send to frontend
def display_webpage(request):
    QLWO=WebPage.objects.all()
    #QLWO=WebPage.objects.all()[::-1]
    #QLWO=WebPage.objects.all().order_by('name')
    #QLWO=WebPage.objects.all().order_by('-name')
    # QLWO=WebPage.objects.all()[:2:] #here we use slicing to find or retrieve data any where on table
    # #QLWO=WebPage.objects.all().order_by(length('name'))
    # #QLWO=WebPage.objects.all().order_by(length('name').desc())# it will arrange the data in descending order in the dat present in name table
    # QLWO=WebPage.objects.all()

    # QLWO=WebPage.objects.filter(id_in=(2,5))

    # QLWO=WebPage.objects.filter(id__range=(2,5))

    # QLWO=WebPage.objects.filter(id__gte=2)

    # QLWO=WebPage.objects.filter(name__startswith='R')

    # QLWO=WebPage.objects.filter(name__endswith='T')

    # QLWO=WebPage.objects.filter(name__contains='R')

    # QLWO=WebPage.objects.filter(name__regex='^r\w*')

    # QLWO=WebPage.objects.filter(name__isnull=False)
    QLWO=WebPage.objects.filter(name__in=('hardik','kohli'))    #here we can use and operator that represents ',' comma
    QLWO=WebPage.objects.filter(Q(name='hardik') | Q(topic_name='cricket')) #here we can use or operator that represents '|'

    d={'QLWO': QLWO }
    return render(request,'display_webpage.html' ,d)
    

def display_topic(request):
    QLTO=Topic.objects.all()
    d={'QLTO': QLTO }
    return render(request,'display_topic.html' ,d)

def display_accessrecord(request):
    QLARO=AccessRecord.objects.all()
    
    #QLAO=AccessRecord.objects.filter(date='2025-10-11')
    QLARO=AccessRecord. objects. filter(date__month='10')
    QLARO=AccessRecord.objects.filter(date__year=2025)
    QLARO=AccessRecord. objects. filter(date__day='11')
    d={'QLARO': QLARO }
    return render(request,'display_accessrecord.html' ,d)
    