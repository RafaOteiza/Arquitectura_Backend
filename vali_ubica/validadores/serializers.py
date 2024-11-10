from rest_framework import serializers
from .models import Ubicacion, EstadoValidador, Validador, SimValidador, HistorialUbicacionesValidador

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

class SimValidadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimValidador
        fields = '__all__'

class HistorialUbicacionesValidadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialUbicacionesValidador
        fields = '__all__'
