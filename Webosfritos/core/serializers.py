from dataclasses import field, fields
from pyexpat import model
from .models import Receta
from rest_framework import serializers

class RecetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receta
        fields = '__all__'