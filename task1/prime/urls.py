from django.urls import path
from prime.views import shows

app_name="shows"
urlpatterns=[
    path('shows/',shows,name='shows'),
    
]