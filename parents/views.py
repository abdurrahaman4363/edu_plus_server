from rest_framework import viewsets
from .models import Parent
from .serializers import ParentSerializer

class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
