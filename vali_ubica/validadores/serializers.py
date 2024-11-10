from rest_framework import serializers
from .models import Ubicacion, EstadoValidador, Validador

class UbicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubicacion
        fields = '__all__'

class EstadoValidadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoValidador
        fields = '__all__'

class ValidadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Validador
        fields = '__all__'
