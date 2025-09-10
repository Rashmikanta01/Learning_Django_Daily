from django.urls import path
from drinks.views import  sprite

app_name="drinks"
urlpatterns=[
    path('sprite/',sprite,name='sprite'),
]