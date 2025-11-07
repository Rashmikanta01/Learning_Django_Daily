"""
URL configuration for modelform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('insert_to_modelform/', insert_to_modelform, name='insert_to_modelform'),
    path('insert_webpageMF/' , insert_webpageMF, name='insert_webpageMF'),
    path('insert_accessMF/', insert_accessMF, name='insert_accessMF'),
    path('insert_countriesMF/', insert_countriesMF, name='insert_countriesMF'),
]
