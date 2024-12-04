from rest_framework import viewsets
from .models import Ubicacion, EstadoValidador, Validador, SimValidador, HistorialUbicacionesValidador
from .serializers import (
    UbicacionSerializer, EstadoValidadorSerializer, ValidadorSerializer, 
    SimValidadorSerializer, HistorialUbicacionesValidadorSerializer
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from django.db import transaction
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

    # Buscar un validador por AMID
    @action(detail=False, methods=['get'])
    def search_by_amid(self, request):
        """
        Endpoint personalizado para buscar un validador por su AMID.
        """
        amid = request.query_params.get('amid', None)
        if not amid:
            return Response({'error': 'Se requiere un parámetro AMID.'}, status=status.HTTP_400_BAD_REQUEST)
        
        validador = self.queryset.filter(amid_val=amid).first()
        if not validador:
            raise NotFound('Validador con el AMID proporcionado no encontrado.')

        serializer = self.serializer_class(validador)
        return Response(serializer.data)

    # Listar validadores con detalles de estado y ubicación
    @action(detail=False, methods=['get'])
    def list_with_details(self, request):
        """
        Endpoint para listar validadores con sus estados y ubicaciones.
        """
        validadores = self.queryset.select_related('id_estado_validador', 'id_ubicacion').all()
        serializer = self.serializer_class(validadores, many=True)
        return Response(serializer.data)

    # Endpoint para manejar carga masiva
    @action(detail=False, methods=['post'])
    def bulk_create(self, request):
        """
        Endpoint para realizar carga masiva de validadores.
        """
        try:
            with transaction.atomic():
                validadores_data = request.data
                if not isinstance(validadores_data, list):
                    return Response({'error': 'Se espera una lista de objetos para la carga masiva.'}, status=status.HTTP_400_BAD_REQUEST)
                
                validadores = []
                for validador_data in validadores_data:
                    serializer = self.serializer_class(data=validador_data)
                    serializer.is_valid(raise_exception=True)
                    validadores.append(serializer.save())

                return Response({'message': f'Se han creado {len(validadores)} validadores con éxito.'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class SimValidadorViewSet(viewsets.ModelViewSet):
    queryset = SimValidador.objects.all()
    serializer_class = SimValidadorSerializer


class HistorialUbicacionesValidadorViewSet(viewsets.ModelViewSet):
    queryset = HistorialUbicacionesValidador.objects.all()
    serializer_class = HistorialUbicacionesValidadorSerializer


class ICCIDListView(APIView):
    def get(self, request):
        """
        Devuelve una lista de ICCIDs disponibles usando la función `obtener_iccids_disponibles`.
        """
        iccids = obtener_iccids_disponibles()
        if iccids:
            return Response({'iccids': iccids}, status=status.HTTP_200_OK)
        return Response({'error': 'No se pudieron obtener los ICCIDs'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
