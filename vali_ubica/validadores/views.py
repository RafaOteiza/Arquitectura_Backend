from rest_framework import viewsets
from .models import Ubicacion, EstadoValidador, Validador, SimValidador, HistorialUbicacionesValidador
from .serializers import (
    UbicacionSerializer, EstadoValidadorSerializer, ValidadorSerializer, 
    SimValidadorSerializer, HistorialUbicacionesValidadorSerializer
)

class UbicacionViewSet(viewsets.ModelViewSet):
    queryset = Ubicacion.objects.all()
    serializer_class = UbicacionSerializer

class EstadoValidadorViewSet(viewsets.ModelViewSet):
    queryset = EstadoValidador.objects.all()
    serializer_class = EstadoValidadorSerializer

class ValidadorViewSet(viewsets.ModelViewSet):
    queryset = Validador.objects.all()
    serializer_class = ValidadorSerializer

class SimValidadorViewSet(viewsets.ModelViewSet):
    queryset = SimValidador.objects.all()
    serializer_class = SimValidadorSerializer

class HistorialUbicacionesValidadorViewSet(viewsets.ModelViewSet):
    queryset = HistorialUbicacionesValidador.objects.all()
    serializer_class = HistorialUbicacionesValidadorSerializer
