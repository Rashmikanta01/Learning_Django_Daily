from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CompanySerializer
from .models import Company


class CompanyCRUD(APIView):

    def get(self, request, pk=None):
        if pk is None:
            qs = Company.objects.all()
            serializer = CompanySerializer(qs, many=True)
            return Response(serializer.data)
        else:
            obj = Company.objects.get(pk=pk)
            serializer = CompanySerializer(obj)
            return Response(serializer.data)

    def post(self, request):

        
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'})
        else:
            return Response(serializer.errors)

    def put(self, request, pk):
        obj = Company.objects.get(pk=pk)
        serializer = CompanySerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Updated'})
        else:
            return Response(serializer.errors)

    def patch(self, request, pk):
        obj = Company.objects.get(pk=pk)
        serializer = CompanySerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Partially Updated'})
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        obj = Company.objects.get(pk=pk)
        obj.delete()
        return Response({'msg': 'Data Deleted'})
