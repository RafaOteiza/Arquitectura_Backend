from django.db import models
from .utils import obtener_datos_usuario


class Ubicacion(models.Model):
    nombre_ubicacion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_ubicacion

class EstadoValidador(models.Model):
    nombre_estado = models.CharField(max_length=100)
    descripcion_estado = models.TextField()

    def __str__(self):
        return self.nombre_estado

class Validador(models.Model):
    serie_val = models.IntegerField(unique=True)
    amid_val = models.IntegerField(unique=True)
    modelo = models.CharField(max_length=5, blank=True, null=True)
    id_ubicacion = models.ForeignKey('Ubicacion', on_delete=models.CASCADE)
    id_estado_validador = models.ForeignKey('EstadoValidador', on_delete=models.CASCADE)
    id_usuario = models.IntegerField()  # ID del usuario que creó el validador
    fecha_creacion = models.DateField()
    usuario_nombre = models.CharField(max_length=100, blank=True, null=True)
    usuario_apellido = models.CharField(max_length=100, blank=True, null=True)
    usuario_correo = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.amid_val}"

    def save(self, *args, **kwargs):
        # Llama a la función para obtener datos del usuario y llenar los campos de usuario
        usuario_data = obtener_datos_usuario(self.id_usuario)
        if usuario_data:
            self.usuario_nombre = usuario_data.get('nombre')
            self.usuario_apellido = usuario_data.get('apellido')
            self.usuario_correo = usuario_data.get('correo')
        super().save(*args, **kwargs)
        
class SimValidador(models.Model):
    iccid = models.CharField(max_length=20)
    amid_val = models.ForeignKey('Validador', on_delete=models.CASCADE, to_field='amid_val')
    inicio_relacion = models.DateField()
    fin_relacion = models.DateField(null=True, blank=True)
    motivo_fin = models.CharField(max_length=20, blank=True, null=True)
    id_usuario = models.IntegerField()  # ID del usuario que creó esta relación
    fecha_creacion = models.DateField()
    usuario_nombre = models.CharField(max_length=100, blank=True, null=True)
    usuario_apellido = models.CharField(max_length=100, blank=True, null=True)
    usuario_correo = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"SIM {self.iccid} - Validador AMID {self.amid_val.amid_val}"

    def save(self, *args, **kwargs):
        # Llama a la función para obtener datos del usuario y llenar los campos de usuario
        usuario_data = obtener_datos_usuario(self.id_usuario)   
        if usuario_data:
            self.usuario_nombre = usuario_data.get('nombre')
            self.usuario_apellido = usuario_data.get('apellido')
            self.usuario_correo = usuario_data.get('correo')
        super().save(*args, **kwargs)

class HistorialUbicacionesValidador(models.Model):
    id_movimiento = models.IntegerField()
    id_validador = models.ForeignKey('Validador', on_delete=models.CASCADE)
    ubicacion_nueva = models.ForeignKey('Ubicacion', on_delete=models.CASCADE)
    fecha_movimiento = models.DateField()
    observacion = models.CharField(max_length=255)
    id_usuario = models.IntegerField()  # ID del usuario que realizó el movimiento
    usuario_nombre = models.CharField(max_length=100, blank=True, null=True)
    usuario_apellido = models.CharField(max_length=100, blank=True, null=True)
    usuario_correo = models.EmailField(blank=True, null=True)

    class Meta:
        unique_together = ('id_movimiento', 'id_validador')

    def __str__(self):
        return f"Movimiento {self.id_movimiento} - Validador {self.id_validador}"

    def save(self, *args, **kwargs):
        # Llama a la función para obtener datos del usuario y llenar los campos de usuario
        usuario_data = obtener_datos_usuario(self.id_usuario)
        if usuario_data:
            self.usuario_nombre = usuario_data.get('nombre')
            self.usuario_apellido = usuario_data.get('apellido')
            self.usuario_correo = usuario_data.get('correo')
        super().save(*args, **kwargs)
