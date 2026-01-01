from django.urls import path
from .views import CompanyCRUD

urlpatterns = [
    path('companies/', CompanyCRUD.as_view()),
    path('companies/<int:pk>/', CompanyCRUD.as_view()),
]
