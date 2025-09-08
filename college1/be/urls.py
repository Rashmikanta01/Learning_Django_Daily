from django.urls import path
from be.views import*
app_name = "something"

urlpatterns = [
    path('student/', student, name="be"),
]