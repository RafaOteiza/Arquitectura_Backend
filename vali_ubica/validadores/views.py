from rest_framework import viewsets
from .models import Ubicacion, EstadoValidador, Validador, SimValidador, HistorialUbicacionesValidador
from .serializers import (
    UbicacionSerializer, EstadoValidadorSerializer, ValidadorSerializer, 
    SimValidadorSerializer, HistorialUbicacionesValidadorSerializer
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import obtener_iccids_disponibles


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

class ICCIDListView(APIView):
    def get(self, request):
        iccids = obtener_iccids_disponibles()
        if iccids:
            return Response({'iccids': iccids}, status=status.HTTP_200_OK)
        return Response({'error': 'No se pudieron obtener los ICCIDs'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
