import secrets

from django.conf import settings
from django.db import models

from apps.core.models import EmpresaModel, TimeStampedModel
from apps.cuentas.models import Seccion


class Plantilla(TimeStampedModel):
    """Plantilla de cuestionario o lista de verificación. La administra Make It MS."""

    nombre = models.CharField(max_length=200)
    norma = models.CharField(max_length=120, blank=True, help_text="Ej. ISO 45001, NOM-030-STPS")
    seccion = models.CharField(max_length=20, choices=Seccion.choices, default=Seccion.AUDITORIA)
    version = models.PositiveIntegerField(default=1)
    activa = models.BooleanField(default=True)
    terminos_referencia = models.TextField(blank=True)

    class Meta:
        ordering = ["nombre", "-version"]

    def __str__(self):
        return f"{self.nombre} v{self.version}"


class Pregunta(models.Model):
    class QuienResponde(models.TextChoices):
        CLIENTE = "cliente", "Cliente"
        AUDITOR = "auditor", "Auditor"
        AMBOS = "ambos", "Ambos"

    class Tipo(models.TextChoices):
        SI_NO = "si_no", "Sí / No / N.A."
        TEXTO = "texto", "Texto"
        NUMERO = "numero", "Número"
        OPCION = "opcion", "Opción múltiple"
        FECHA = "fecha", "Fecha"
        ARCHIVO = "archivo", "Solo archivo"

    class PuntoInspeccion(models.TextChoices):
        NINGUNO = "", "Sin punto"
        HOLD = "H", "Hold (detiene trabajo)"
        WITNESS = "W", "Witness (se invita)"
        REVIEW = "R", "Review (revisión documental)"

    plantilla = models.ForeignKey(Plantilla, on_delete=models.CASCADE, related_name="preguntas")
    orden = models.PositiveIntegerField(default=0)
    apartado = models.CharField(max_length=120, blank=True)
    texto = models.TextField()
    ayuda = models.TextField(blank=True)
    tipo = models.CharField(max_length=10, choices=Tipo.choices, default=Tipo.SI_NO)
    opciones = models.JSONField(default=list, blank=True)
    quien_responde = models.CharField(max_length=10, choices=QuienResponde.choices, default=QuienResponde.CLIENTE)
    punto_inspeccion = models.CharField(max_length=1, choices=PuntoInspeccion.choices, default="", blank=True)
    requiere_evidencia = models.BooleanField(default=False)
    peso = models.DecimalField(max_digits=5, decimal_places=2, default=1)

    class Meta:
        ordering = ["plantilla", "orden"]

    def __str__(self):
        return self.texto[:80]


def _token():
    return secrets.token_urlsafe(32)


class Auditoria(EmpresaModel):
    class Estatus(models.TextChoices):
        BORRADOR = "borrador", "Borrador"
        ENVIADA = "enviada", "Enviada al cliente"
        REVISION = "revision", "En revisión"
        VISITA = "visita", "Visita"
        CERRADA = "cerrada", "Cerrada"

    proyecto = models.ForeignKey("cuentas.Proyecto", on_delete=models.PROTECT, related_name="auditorias")
    plantilla = models.ForeignKey(Plantilla, on_delete=models.PROTECT)
    preguntas_congeladas = models.JSONField(
        default=list, blank=True, help_text="Copia de las preguntas al crear la auditoría."
    )
    titulo = models.CharField(max_length=200)
    auditor = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, blank=True, related_name="auditorias_asignadas"
    )
    fecha_programada = models.DateField(null=True, blank=True)
    fecha_limite_cliente = models.DateField(null=True, blank=True)
    estatus = models.CharField(max_length=10, choices=Estatus.choices, default=Estatus.BORRADOR)
    token_cliente = models.CharField(max_length=64, unique=True, default=_token, editable=False)
    calificacion = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    class Meta:
        ordering = ["-fecha_programada", "-creado"]
        verbose_name = "auditoría"

    def __str__(self):
        return self.titulo

    def congelar_preguntas(self):
        self.preguntas_congeladas = list(
            self.plantilla.preguntas.values(
                "id", "orden", "apartado", "texto", "tipo", "opciones",
                "quien_responde", "punto_inspeccion", "requiere_evidencia", "peso",
            )
        )
        for p in self.preguntas_congeladas:
            p["peso"] = str(p["peso"])


class Respuesta(TimeStampedModel):
    class Estatus(models.TextChoices):
        PENDIENTE = "pendiente", "Pendiente"
        CLIENTE = "cliente", "Respondida por cliente"
        VERIFICADA = "verificada", "Verificada por auditor"
        HALLAZGO = "hallazgo", "Con hallazgo"

    auditoria = models.ForeignKey(Auditoria, on_delete=models.CASCADE, related_name="respuestas")
    pregunta_id_original = models.PositiveIntegerField()
    valor_cliente = models.TextField(blank=True)
    valor_auditor = models.TextField(blank=True, help_text="Corrección del auditor; no borra la del cliente.")
    comentario_auditor = models.TextField(blank=True)
    estatus = models.CharField(max_length=10, choices=Estatus.choices, default=Estatus.PENDIENTE)
    respondido_por = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="+"
    )

    class Meta:
        unique_together = [("auditoria", "pregunta_id_original")]
