from rest_framework import viewsets
from .models import MSISDN, SimMsisdn, EstadoSim
from .serializers import MSISDNSerializer, SimMsisdnSerializer, EstadoSimSerializer
from django.shortcuts import render

# probando si funciona llamar a la api
from rest_framework.response import Response
from .utils import obtener_usuario, obtener_todos
from rest_framework.views import APIView


class MSISDNViewSet(viewsets.ModelViewSet):
    queryset = MSISDN.objects.all()
    serializer_class = MSISDNSerializer

class SimMsisdnViewSet(viewsets.ModelViewSet):
    queryset = SimMsisdn.objects.all()
    serializer_class = SimMsisdnSerializer

class EstadoSimViewSet(viewsets.ModelViewSet):
    queryset = EstadoSim.objects.all()
    serializer_class = EstadoSimSerializer

class TestUsuarioView(APIView):
    def get(self, request, id_usuario):
        # Llama a la función `obtener_usuario` para obtener los datos
        usuario = obtener_usuario(id_usuario)
        if usuario:
            return Response(usuario)
        else:
            return Response({"error": "Usuario no encontrado o no se pudo conectar a usuarios_auth"}, status=404)
        
def index(request):

    usuarioo = obtener_todos()
 # Aqui tengo que ejecutar las funciones del crud aa que retornen los datos que necesito para la plantilla :p
    return render(request, 'index.html', {'usuario': usuarioo})


