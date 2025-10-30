from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def htmlform(request):
    if request.method=='POST':
        un=request.POST['una']
        pw=request.POST['pwa']
        return HttpResponse(f'username:{un} and password:{pw}')
    
    return render(request,'htmlform.html')
