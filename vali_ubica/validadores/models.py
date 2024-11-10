from django.db import models

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
    id_ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    id_estado_validador = models.ForeignKey(EstadoValidador, on_delete=models.CASCADE)
    id_usuario = models.IntegerField()  # Guardará el ID del usuario que creó el validador
    fecha_creacion = models.DateField()

    def __str__(self):
        return f"Validador {self.serie_val}"

class SimValidador(models.Model):
    iccid = models.CharField(max_length=20)
    amid_val = models.ForeignKey(Validador, on_delete=models.CASCADE, to_field='amid_val')
    inicio_relacion = models.DateField()
    fin_relacion = models.DateField(null=True, blank=True)
    motivo_fin = models.CharField(max_length=20, blank=True, null=True)
    id_usuario = models.IntegerField()  # ID del usuario que creó esta relación
    fecha_creacion = models.DateField()

    def __str__(self):
        return f"SIM {self.iccid} - Validador {self.amid_val}"

class HistorialUbicacionesValidador(models.Model):
    id_movimiento = models.IntegerField()
    id_validador = models.ForeignKey(Validador, on_delete=models.CASCADE)
    ubicacion_nueva = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    fecha_movimiento = models.DateField()
    observacion = models.CharField(max_length=255)
    id_usuario = models.IntegerField()  # ID del usuario que realizó el movimiento

    class Meta:
        unique_together = ('id_movimiento', 'id_validador')

    def __str__(self):
        return f"Movimiento {self.id_movimiento} - Validador {self.id_validador}"
