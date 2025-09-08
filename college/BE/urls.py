from django.urls import path
from BE.views import*
app-name = "something"

urlpatterns = [
    path('be/', be, name="be"),
]