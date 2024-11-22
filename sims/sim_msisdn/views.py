from rest_framework import viewsets, filters
from .models import MSISDN, SimMsisdn, EstadoSim
from .serializers import MSISDNSerializer, SimMsisdnSerializer, EstadoSimSerializer

class MSISDNViewSet(viewsets.ModelViewSet):
    queryset = MSISDN.objects.all()
    serializer_class = MSISDNSerializer

class SimMsisdnViewSet(viewsets.ModelViewSet):
    queryset = SimMsisdn.objects.all()
    serializer_class = SimMsisdnSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['iccid']  # Permite buscar por el campo iccid
    search_fields = ['msisdn']
    
class EstadoSimViewSet(viewsets.ModelViewSet):
    queryset = EstadoSim.objects.all()
    serializer_class = EstadoSimSerializer
