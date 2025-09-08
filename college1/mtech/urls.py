from django.urls import path
from mtech.views import*
app_name = "something_01245"

urlpatterns = [
    path('student/', student, name="btech"),
]