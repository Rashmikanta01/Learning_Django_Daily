from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def student(request):
    return HttpResponse("<h1>ME student</h1>")