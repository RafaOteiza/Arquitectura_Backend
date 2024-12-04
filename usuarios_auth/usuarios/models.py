from django.db import models

class Roles(models.Model):
    nombre_rol = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_rol

class Usuarios(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100, unique=True)
    contraseña = models.CharField(max_length=100)
    id_rol = models.ForeignKey(Roles, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
