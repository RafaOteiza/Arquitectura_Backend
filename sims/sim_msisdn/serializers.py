from rest_framework import serializers
from .models import MSISDN, SimMsisdn, EstadoSim

# Serializador para EstadoSim
class EstadoSimSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoSim
        fields = '__all__'

# Serializador para MSISDN
class MSISDNSerializer(serializers.ModelSerializer):
    class Meta:
        model = MSISDN
        fields = [
            'msisdn', 'nodo_concert_ip', 'nodo_condor_ip', 
            'id_usuario', 'fecha_creacion', 
            'usuario_nombre', 'usuario_apellido', 'usuario_correo'
        ]
        read_only_fields = ['usuario_nombre', 'usuario_apellido', 'usuario_correo']

# Serializador para SimMsisdn
class SimMsisdnSerializer(serializers.ModelSerializer):
    id_msisdn = MSISDNSerializer()  # Serializa los detalles completos de MSISDN
    id_estado = EstadoSimSerializer()  # Serializa los detalles completos del EstadoSim

    class Meta:
        model = SimMsisdn
        fields = [
            'iccid', 'id_msisdn', 'inicio_relacion', 'fin_relacion',
            'motivo_fin', 'id_estado', 'id_usuario', 'fecha_creacion',
            'usuario_nombre', 'usuario_apellido', 'usuario_correo'
        ]
        read_only_fields = ['usuario_nombre', 'usuario_apellido', 'usuario_correo']
