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
    # Agregamos los nombres de los estados y ubicaciones como campos adicionales
    estado_validador_nombre = serializers.CharField(source='id_estado_validador.nombre_estado', read_only=True)
    ubicacion_nombre = serializers.CharField(source='id_ubicacion.nombre_ubicacion', read_only=True)

    class Meta:
        model = Validador
        fields = [
            'id', 'serie_val', 'amid_val', 'modelo', 'id_usuario', 'fecha_creacion',
            'usuario_nombre', 'usuario_apellido', 'usuario_correo', 
            'id_ubicacion', 'ubicacion_nombre',  # Incluimos el nombre de la ubicación
            'id_estado_validador', 'estado_validador_nombre'  # Incluimos el nombre del estado
        ]
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
