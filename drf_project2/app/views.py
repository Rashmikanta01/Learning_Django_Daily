from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from app.serializers import *
from .models import *
# Create your views here.

class StudentCRUD(APIView):
    def get(self,request,pk=None):
        if pk == None:
            QSLSO=Student.objects.all()
            SJD=StudentMS(QSLSO,many=True)
            return Response(SJD.data)
        else:
            SO=Student.objects.get(pk=pk)
            JO=StudentMS(SO)
            return Response(JO.data)
        
    def post(self,request,pk=None):
        SJD=request.data
        PDO=StudentMS(data=SJD)
        if PDO.is_valid():
            PDO.save()
            return Response({'msg':'Data Created'})
        else:
            return Response({'Failed':'issues while inserting'})

    def put(self,request,pk):
        pk=request.data
        SO=Student.objects.get(pk=pk)
        USO=StudentMS(SO,data=request.data)
        if USO.is_valid():
            USO.save()
            return Response({'msg':'Data Updated'})
        else:
            return Response({'Failed':'issues while updating'})
        
    def patch(self,request,pk):
        pk=request.data
        SO=Student.objects.get(pk=pk)
        USO=StudentMS(SO,data=request.data,partial=True)
        if USO.is_valid():
            USO.save()
            return Response({'msg':'Data Partially Updated'})
        
        
    def delete(self,request,pk):
        SO=Student.objects.get(pk=pk)
        SO.delete()
        return Response({'msg':'Data Deleted'})