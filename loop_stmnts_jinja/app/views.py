from django.shortcuts import render

# Create your views here.
def loops(request):
    d={'name':'rashmi kanta', 'name2':'akash'}
    
    return render(request,'loops.html',d)


