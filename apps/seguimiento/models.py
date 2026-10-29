"""Entidad común de seguimiento.

Hallazgos, no conformidades (NCR), observaciones de recorrido, incidentes,
accidentes y riesgos son un `Asunto` con distinto `origen` y `tipo`.
Un solo tablero cubre todo.
"""

from django.conf import settings
from django.db import models

from apps.core.models import EmpresaModel, TimeStampedModel


class Asunto(EmpresaModel):
    class Origen(models.TextChoices):
        AUDITORIA = "auditoria", "Auditoría"
        INSPECCION = "inspeccion", "Inspección"
        RECORRIDO = "recorrido", "Recorrido QAQC / obra / precomisionado"
        INCIDENTE = "incidente", "Incidente"
        ACCIDENTE = "accidente", "Accidente"
        RIESGO = "riesgo", "Riesgo"

    class Tipo(models.TextChoices):
        HALLAZGO = "hallazgo", "Hallazgo"
        NCR = "ncr", "No conformidad (NCR)"
        OBSERVACION = "observacion", "Observación"
        OPORTUNIDAD = "oportunidad", "Oportunidad de mejora"

    class Severidad(models.TextChoices):
        BAJA = "baja", "Baja"
        MEDIA = "media", "Media"
        ALTA = "alta", "Alta"
        CRITICA = "critica", "Crítica"

    class Estatus(models.TextChoices):
        ABIERTO = "abierto", "Abierto"
        EN_ATENCION = "en_atencion", "En atención"
        POR_VERIFICAR = "por_verificar", "Por verificar eficacia"
        CERRADO = "cerrado", "Cerrado"

    proyecto = models.ForeignKey("cuentas.Proyecto", on_delete=models.PROTECT, related_name="asuntos")
    auditoria = models.ForeignKey(
        "auditorias.Auditoria", on_delete=models.SET_NULL, null=True, blank=True, related_name="asuntos"
    )
    origen = models.CharField(max_length=12, choices=Origen.choices)
    tipo = models.CharField(max_length=12, choices=Tipo.choices, default=Tipo.HALLAZGO)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    severidad = models.CharField(max_length=8, choices=Severidad.choices, default=Severidad.MEDIA)
    ubicacion = models.CharField(max_length=200, blank=True, help_text="Frente, área o nivel.")
    latitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    responsable = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="asuntos_asignados"
    )
    fecha_limite = models.DateField(null=True, blank=True)
    estatus = models.CharField(max_length=14, choices=Estatus.choices, default=Estatus.ABIERTO)
    # CAPA
    causa_raiz = models.TextField(blank=True)
    accion_correctiva = models.TextField(blank=True)
    accion_preventiva = models.TextField(blank=True)
    eficacia_verificada = models.BooleanField(default=False)
    leccion_aprendida = models.TextField(blank=True)

    class Meta:
        ordering = ["estatus", "fecha_limite"]

    def __str__(self):
        return self.titulo


class Evidencia(TimeStampedModel):
    """Foto o archivo ligado a una respuesta de auditoría o a un asunto."""

    respuesta = models.ForeignKey(
        "auditorias.Respuesta", on_delete=models.CASCADE, null=True, blank=True, related_name="evidencias"
    )
    asunto = models.ForeignKey(Asunto, on_delete=models.CASCADE, null=True, blank=True, related_name="evidencias")
    archivo = models.FileField(upload_to="evidencias/%Y/%m/")
    descripcion = models.CharField(max_length=200, blank=True)
    subido_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="+")

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=models.Q(respuesta__isnull=False) | models.Q(asunto__isnull=False),
                name="evidencia_con_dueno",
            )
        ]
