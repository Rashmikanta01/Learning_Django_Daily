from django.urls import path
from btech.views import*
app_name = "something_012"

urlpatterns = [
    path('student/', student, name="btech"),
]