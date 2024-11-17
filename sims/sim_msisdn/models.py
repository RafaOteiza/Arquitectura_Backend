from django.db import models
import requests
from django.conf import settings
from .utils import obtener_datos_usuario  


class EstadoSim(models.Model):
    nombre_estado = models.CharField(max_length=100)
    descripcion_estado = models.TextField()

    def __str__(self):
        return self.nombre_estado

class MSISDN(models.Model):
    msisdn = models.CharField(max_length=20, unique=True)
    nodo_concert_ip = models.CharField(max_length=15)
    nodo_condor_ip = models.CharField(max_length=15)
    id_usuario = models.IntegerField()  
    fecha_creacion = models.DateField()
    usuario_nombre = models.CharField(max_length=100, blank=True, null=True)
    usuario_apellido = models.CharField(max_length=100, blank=True, null=True)
    usuario_correo = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.msisdn

    def save(self, *args, **kwargs):
        # Llama a la función para obtener datos del usuario y llenar los campos de usuario
        usuario_data = obtener_datos_usuario(self.id_usuario)
        if usuario_data:
            self.usuario_nombre = usuario_data.get('nombre')
            self.usuario_apellido = usuario_data.get('apellido')
            self.usuario_correo = usuario_data.get('correo')
        super().save(*args, **kwargs)

class SimMsisdn(models.Model):
    iccid = models.CharField(max_length=20, unique=True)
    id_msisdn = models.ForeignKey('MSISDN', on_delete=models.CASCADE)
    inicio_relacion = models.DateField()
    fin_relacion = models.DateField(null=True, blank=True)
    motivo_fin = models.CharField(max_length=20, blank=True, null=True)
    id_estado = models.ForeignKey('EstadoSim', on_delete=models.CASCADE)
    id_usuario = models.IntegerField() 
    fecha_creacion = models.DateField()
    usuario_nombre = models.CharField(max_length=100, blank=True, null=True)
    usuario_apellido = models.CharField(max_length=100, blank=True, null=True)
    usuario_correo = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.iccid

    def save(self, *args, **kwargs):
        # Llama a la función para obtener datos del usuario
        usuario_data = obtener_datos_usuario(self.id_usuario)
        if usuario_data:
            self.usuario_nombre = usuario_data.get('nombre')
            self.usuario_apellido = usuario_data.get('apellido')
            self.usuario_correo = usuario_data.get('correo')
        super().save(*args, **kwargs)