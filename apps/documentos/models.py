"""Control documental (fase 2). El modelo va desde ya para no migrar después.

Búsqueda por metadatos (JSONB) y por contenido (tsvector en español).
El texto se extrae en segundo plano con django-q2 al subir el archivo.
"""

from django.conf import settings
from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVectorField
from django.db import models

from apps.core.models import EmpresaModel
from apps.cuentas.models import Seccion


class Documento(EmpresaModel):
    class Estado(models.TextChoices):
        TRABAJO = "trabajo", "Trabajo en curso"
        COMPARTIDO = "compartido", "Compartido"
        PUBLICADO = "publicado", "Publicado"
        ARCHIVADO = "archivado", "Archivado"

    proyecto = models.ForeignKey("cuentas.Proyecto", on_delete=models.PROTECT, related_name="documentos")
    seccion = models.CharField(max_length=20, choices=Seccion.choices)
    codigo = models.CharField(max_length=80, blank=True, help_text="Nomenclatura del proyecto.")
    titulo = models.CharField(max_length=200)
    tipo = models.CharField(max_length=80, blank=True, help_text="Procedimiento, plano, certificado…")
    revision = models.CharField(max_length=10, default="0")
    estado = models.CharField(max_length=12, choices=Estado.choices, default=Estado.TRABAJO)
    archivo = models.FileField(upload_to="documentos/%Y/%m/")
    metadatos = models.JSONField(default=dict, blank=True)
    texto_extraido = models.TextField(blank=True, editable=False)
    busqueda = SearchVectorField(null=True, editable=False)
    subido_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="+")

    class Meta:
        ordering = ["proyecto", "codigo", "-revision"]
        indexes = [GinIndex(fields=["busqueda"]), GinIndex(fields=["metadatos"])]

    def __str__(self):
        return f"{self.codigo or self.titulo} rev {self.revision}"
