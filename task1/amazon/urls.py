from django.urls import path
from amazon.views import electronics

app_name="electronics"
urlpatterns=[
    path('electronics/',electronics,name='electronics'),
    
]