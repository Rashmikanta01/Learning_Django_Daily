from django.shortcuts import render
from django.views.generic import *
from app.forms import *
from django.http import HttpResponse

# Create your views here.
class RenderHtmlByTV(TemplateView):
    template_name = 'RenderHtmlByTV.html'
    def get_context_data(self, **kwargs):
        ECDO= super().get_context_data(**kwargs)
        ECDO['name']= 'Django QSP'
        ECDO['course']= 'Django Full Stack Development'
        return ECDO
class insertByTV(TemplateView):
    template_name = 'insertByTV.html'
    def get_context_data(self, **kwargs):
        ECDO= super().get_context_data(**kwargs)
        ECDO['ESMFO']= StudentForm()
        return ECDO
    def post(self, request):
        SMFDO= StudentForm(request.POST)
        if SMFDO.is_valid():
            SMFDO.save()
            return HttpResponse('Data Inserted Successfully')
        else:
            return HttpResponse('Data Insertion Failed')