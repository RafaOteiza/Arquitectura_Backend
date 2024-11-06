from rest_framework import serializers
from .models import MSISDN, SimMsisdn, EstadoSim

class MSISDNSerializer(serializers.ModelSerializer):
    class Meta:
        model = MSISDN
        fields = '__all__'

class SimMsisdnSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimMsisdn
        fields = '__all__'

class EstadoSimSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoSim
        fields = '__all__'
