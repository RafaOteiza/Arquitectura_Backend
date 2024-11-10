from rest_framework import viewsets
from .models import Ubicacion, EstadoValidador, Validador
from .serializers import UbicacionSerializer, EstadoValidadorSerializer, ValidadorSerializer

class UbicacionViewSet(viewsets.ModelViewSet):
    queryset = Ubicacion.objects.all()
    serializer_class = UbicacionSerializer

class EstadoValidadorViewSet(viewsets.ModelViewSet):
    queryset = EstadoValidador.objects.all()
    serializer_class = EstadoValidadorSerializer

class ValidadorViewSet(viewsets.ModelViewSet):
    queryset = Validador.objects.all()
    serializer_class = ValidadorSerializer
