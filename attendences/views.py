from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers

# Create your views here.
class AttendenceViewSet(viewsets.ModelViewSet):
    queryset = models.Attendence.objects.all()
    serializer_class = serializers.CourseSerializer
