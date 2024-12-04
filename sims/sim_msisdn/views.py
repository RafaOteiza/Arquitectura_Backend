
from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import MSISDN, SimMsisdn, EstadoSim
from .serializers import MSISDNSerializer, SimMsisdnSerializer, EstadoSimSerializer

class MSISDNViewSet(viewsets.ModelViewSet):
    queryset = MSISDN.objects.all()
    serializer_class = MSISDNSerializer


class SimMsisdnViewSet(viewsets.ModelViewSet):
    queryset = SimMsisdn.objects.all()
    serializer_class = SimMsisdnSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['iccid']  # Permite buscar por ICCID
    search_fields = ['msisdn']

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


class EstadoSimViewSet(viewsets.ModelViewSet):
    queryset = EstadoSim.objects.all()
    serializer_class = EstadoSimSerializer
