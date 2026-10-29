from django.db import models

from apps.core.models import TimeStampedModel


class SolicitudCotizacion(TimeStampedModel):
    class Servicio(models.TextChoices):
        AUDITORIAS = "auditorias", "Auditorías"
        SEGURIDAD = "seguridad", "Seguridad"
        SUSTENTABILIDAD = "sustentabilidad", "Sustentabilidad"
        VARIOS = "varios", "Varios servicios"

    class Estatus(models.TextChoices):
        NUEVA = "nueva", "Nueva"
        CONTACTADA = "contactada", "Contactada"
        COTIZADA = "cotizada", "Cotizada"
        DESCARTADA = "descartada", "Descartada"

    nombre = models.CharField(max_length=120)
    empresa = models.CharField(max_length=160)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True)
    servicio = models.CharField(max_length=16, choices=Servicio.choices)
    mensaje = models.TextField(blank=True)
    estatus = models.CharField(max_length=12, choices=Estatus.choices, default=Estatus.NUEVA)

    class Meta:
        ordering = ["-creado"]
        verbose_name = "solicitud de cotización"
        verbose_name_plural = "solicitudes de cotización"

    def __str__(self):
        return f"{self.empresa} · {self.get_servicio_display()}"
