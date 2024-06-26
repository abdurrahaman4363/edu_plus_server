from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers

# Create your views here.
class TeacherViewSet(viewsets.ModelViewSet):
    queryset = models.Teacher.objects.all()
    serializer_class = serializers.TeacherSerializer
