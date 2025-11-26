from django.shortcuts import render
from django.http import HttpResponse
from app.forms import schoolMF
from django.views.generic import View

# Create your views here.
#i can create bothe class based views and function based views here
# so first i create a function based view
def fview(request):
    return HttpResponse("<h1>This is a function based view</h1>")

# now i create a class based view
class Cview(View):   
    def get(self, request):
        return HttpResponse("<h1>This is a class based view</h1>")
    
#returning a template using function based view
def fbtemp(request):
    return render(request, 'fbtemp.html')

#returning a template using class based view
class cbtemp(View):
    def get(self, request):
        return render(request, 'cbtemp.html')
    
#validating a form using function based view
def fbform(request):
    form = schoolMF()
    if request.method == 'POST':
        form = schoolMF(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(str(form.cleaned_data))
    return render(request, 'fbform.html',context={'form':form})

#validating a form using class based view
class cbform(View):
    def get(self, request):
        form = schoolMF()
        return render(request, 'cbform.html',context={'form':form})
    
    def post(self, request):
        form = schoolMF(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(str(form.cleaned_data))
        return render(request, 'cbform.html',context={'form':form})


