from rest_framework import serializers
from Webosfritos.core.models import Receta
from core.models import Receta

class MascotaSerializers2(serializers.ModelSerializer):
    class Meta:
        model = Receta
        fields = ['titulo','imagen','parrafo','usuario']