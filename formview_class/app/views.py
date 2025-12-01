from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import FormView
from app.forms import *
from django.http import HttpResponse



class StudentFormView(FormView):
    template_name = 'student_formview.html'
    form_class = StudentForm
    

    def form_valid(self, form):
        form.save()
        return HttpResponse("Student data saved successfully!")
    def form_invalid(self, form):
        return HttpResponse("Invalid data submitted.")