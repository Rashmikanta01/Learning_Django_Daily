from django.shortcuts import render
from app.serializer import *
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# Create your views here.
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])

def SchoolApiView(request):
    QSLSO=School.objects.all()
    JSO=SchoolMS(QSLSO,many=True)
    jd=JSO.data
    return Response(jd)