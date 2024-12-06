
from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import MSISDN, SimMsisdn, EstadoSim
from .serializers import MSISDNSerializer, SimMsisdnSerializer, EstadoSimSerializer

class MSISDNViewSet(viewsets.ModelViewSet):
    queryset = MSISDN.objects.all()
    serializer_class = MSISDNSerializer


from rest_framework.decorators import action
from rest_framework.response import Response
from .models import SimMsisdn, MSISDN
from .serializers import SimMsisdnSerializer
from rest_framework import filters, status
from rest_framework import viewsets


class SimMsisdnViewSet(viewsets.ModelViewSet):
    queryset = SimMsisdn.objects.all()
    serializer_class = SimMsisdnSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['iccid', 'msisdn']  # Permite buscar por ICCID y MSISDN

    @action(detail=False, methods=['put'], url_path='update-by-iccid')
    def update_by_iccid(self, request):
        """
        Actualiza el MSISDN asociado a una SIM utilizando el ICCID proporcionado.
        """
        iccid = request.data.get('iccid')
        msisdn = request.data.get('msisdn')  # Nuevo valor del MSISDN

        if not iccid:
            return Response({"error": "ICCID no proporcionado."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            sim = SimMsisdn.objects.get(iccid=iccid)
        except SimMsisdn.DoesNotExist:
            return Response({"error": "SIM no encontrada."}, status=status.HTTP_404_NOT_FOUND)

        if msisdn is None:  # Disociar el MSISDN
            sim.id_msisdn = None
        else:
            try:
                msisdn_instance = MSISDN.objects.get(msisdn=msisdn)
                sim.id_msisdn = msisdn_instance
            except MSISDN.DoesNotExist:
                return Response({"error": "MSISDN no encontrado."}, status=status.HTTP_404_NOT_FOUND)

        sim.save()
        serializer = self.get_serializer(sim)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='buscar-por-amid')
    def buscar_por_amid(self, request):
        """
        Devuelve todos los ICCIDs asociados a un validador por su `amid_val`.
        """
        amid_val = request.query_params.get('amid_val')
        if not amid_val:
            return Response({"error": "El parámetro 'amid_val' es requerido."}, status=status.HTTP_400_BAD_REQUEST)

        sims = SimMsisdn.objects.filter(amid_val=amid_val)
        if not sims.exists():
            return Response({"error": "No se encontraron SIMs asociadas al AMID proporcionado."}, status=status.HTTP_404_NOT_FOUND)

        serializer = SimMsisdnSerializer(sims, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class EstadoSimViewSet(viewsets.ModelViewSet):
    queryset = EstadoSim.objects.all()
    serializer_class = EstadoSimSerializer
