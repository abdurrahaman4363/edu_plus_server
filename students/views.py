from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer


class StudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
# dd 