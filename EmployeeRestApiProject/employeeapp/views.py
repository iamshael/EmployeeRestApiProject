from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponse
from .models import Employee
from .serializers import EmployeeSerializer

# Create your views here.
def helloview(request):
    return HttpResponse("Hello Shailesh...")

@api_view(['GET','POST'])
def empview(request):
    if request.method == 'GET':
        emp_data = Employee.objects.all()
        serializer = EmployeeSerializer(emp_data,many=True)
        return Response(serializer.data)
    elif request.method =="POST":
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)