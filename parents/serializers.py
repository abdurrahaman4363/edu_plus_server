from rest_framework import serializers
from .models import Parent

class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = '__all__'
