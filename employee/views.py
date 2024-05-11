from rest_framework import viewsets
from . import models
from . import serializers

# from django.shortcuts import render

# Create your views here.


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
