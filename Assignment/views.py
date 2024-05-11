from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers

# Create your views here.
class TeacherViewSet(viewsets.ModelViewSet):
    queryset = models.Assignment.objects.all()
    serializer_class = serializers.AssignmentSerializer