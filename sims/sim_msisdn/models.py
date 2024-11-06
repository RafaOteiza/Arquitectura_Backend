from django.db import models

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

    def __str__(self):
        return self.msisdn

class SimMsisdn(models.Model):
    iccid = models.CharField(max_length=20, unique=True)
    id_msisdn = models.ForeignKey(MSISDN, on_delete=models.CASCADE)
    inicio_relacion = models.DateField()
    fin_relacion = models.DateField(null=True, blank=True)
    motivo_fin = models.CharField(max_length=20, blank=True, null=True)
    id_estado = models.ForeignKey(EstadoSim, on_delete=models.CASCADE)
    id_usuario = models.IntegerField() 
    fecha_creacion = models.DateField()

    def __str__(self):
        return self.iccid
