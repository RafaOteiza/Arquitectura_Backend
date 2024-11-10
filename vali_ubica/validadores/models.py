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

    def save(self, *args, **kwargs):
        # Puedes agregar lógica adicional aquí si necesitas completar datos automáticamente
        super().save(*args, **kwargs)
