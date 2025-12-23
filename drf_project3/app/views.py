from django.shortcuts import render
#this is viewsets importing
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.response import Response

# Create your views here.
class  StudentCRUDBYViewSet(viewsets):
    def list(self, request):
        QSLSO=Student.objects.all()
        SJD=StudentMS(QSLSO,many=True)
        return Response(SJD.data)
    def retrieve(self, request, pk=None):
        QSLSO=Student.objects.get(id=pk)
        SJD=StudentMS(QSLSO)
        return Response(SJD.data)
    
    def create(self, request):
        SJD=StudentMS(data=request.data)
        if SJD.is_valid():
            SJD.save()
            return Response({"msg":"Data Created"})
        else:
            return Response({'msg':"Data Not Created"})

    def update(self, request, pk=None):
        QSLSO=Student.objects.get(id=pk)
        SJD=StudentMS(QSLSO,data=request.data)
        if SJD.is_valid():
            SJD.save()
            return Response({"msg":"Data Updated"})
        else:
            return Response({'msg':"Data Not Updated"})
    def partial_update(self, request, pk=None):
        QSLSO=Student.objects.get(id=pk)
        SJD=StudentMS(QSLSO,data=request.data,partial=True)
        if SJD.is_valid():
            SJD.save()
            return Response({"msg":"Data Partially Updated"})
        else:
            return Response({'msg':"Data Not Updated"})
        
    def destroy(self, request, pk=None):
        QSLSO=Student.objects.get(id=pk)
        QSLSO.delete()
        return Response({"msg":"Data Deleted"})
    
class StudentGAVViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentMS