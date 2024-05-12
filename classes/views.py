from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers

# Create your views here.
class ClassesViewSet(viewsets.ModelViewSet):
    queryset = models.Classes.objects.all()
    serializer_class = serializers.CourseSerializer
