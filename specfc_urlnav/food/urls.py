from django.urls import path
from food.views import biriyani

app_name="food"
urlpatterns=[
    path('biriyani/',biriyani,name='biriyani'),
    
]