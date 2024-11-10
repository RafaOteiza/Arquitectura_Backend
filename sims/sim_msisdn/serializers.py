from rest_framework import serializers
from .models import MSISDN, SimMsisdn, EstadoSim

class MSISDNSerializer(serializers.ModelSerializer):
    class Meta:
        model = MSISDN
        fields = '__all__'

class SimMsisdnSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimMsisdn
        fields = [
            'iccid', 'id_msisdn', 'inicio_relacion', 'fin_relacion', 
            'motivo_fin', 'id_estado', 'id_usuario', 'fecha_creacion',
            'usuario_nombre', 'usuario_apellido', 'usuario_correo'
        ]
        read_only_fields = ['usuario_nombre', 'usuario_apellido', 'usuario_correo']

class EstadoSimSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoSim
        fields = '__all__'
