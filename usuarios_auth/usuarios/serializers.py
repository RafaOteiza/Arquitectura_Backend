from rest_framework import serializers
from .models import Usuarios, Roles

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'  # Incluir todos los campos de Roles

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ['nombre', 'apellido', 'correo', 'contraseña', 'id_rol']  # Campos que quieres exponer
