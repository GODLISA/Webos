from core.models import Receta, Usuario
from rest_framework import serializers

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class RecetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receta
        fields = ['idreceta','titulo', 'parrafo', 'usuario']