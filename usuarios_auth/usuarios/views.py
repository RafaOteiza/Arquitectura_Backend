from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Usuarios, Roles
from .serializers import UsuarioSerializer, RolSerializer

class RolViewSet(viewsets.ModelViewSet):
    queryset = Roles.objects.all()
    serializer_class = RolSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuarioSerializer

    # Personaliza el filtrado
    def get_queryset(self):
        queryset = super().get_queryset()
        correo = self.request.query_params.get('correo', None)
        contraseña = self.request.query_params.get('contraseña', None)

        if correo and contraseña:
            queryset = queryset.filter(correo=correo, contraseña=contraseña)
        return queryset
