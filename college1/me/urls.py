
from django.urls import path
from me.views import*
app_name = "something_555"

urlpatterns = [
    path('student/', student, name="me"),
]