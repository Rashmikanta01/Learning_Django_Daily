from django.shortcuts import render

# Create your views here.
def shows(request):
    return render (request,'prime.html')

