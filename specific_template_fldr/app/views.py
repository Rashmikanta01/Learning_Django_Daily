from django.shortcuts import render
from app.models import school
from django.views.generic import ListView, DetailView


# List view for all schools
class SchoolListView(ListView):
    model = school
    context_object_name = 'schools'
    
    # ordering = ['name']


# Detail view for a single school
class SchoolDetailView(DetailView):
    model = school
    context_object_name = 'school'
    
