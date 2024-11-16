from rest_framework import serializers
from .models import Ubicacion, EstadoValidador, Validador, SimValidador, HistorialUbicacionesValidador
from .utils import obtener_iccids_disponibles

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
        read_only_fields = ['usuario_nombre', 'usuario_apellido', 'usuario_correo']


class SimValidadorSerializer(serializers.ModelSerializer):
    iccid = serializers.ChoiceField(choices=[], required=True)  # Sobrescribe el campo con opciones dinámicas

    class Meta:
        model = SimValidador
        fields = '__all__'
        read_only_fields = ['usuario_nombre', 'usuario_apellido', 'usuario_correo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Poblar dinámicamente las opciones de ICCID al inicializar el serializador
        self.fields['iccid'].choices = [(iccid, iccid) for iccid in obtener_iccids_disponibles()]


class HistorialUbicacionesValidadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialUbicacionesValidador
        fields = '__all__'
        read_only_fields = ['usuario_nombre', 'usuario_apellido', 'usuario_correo']