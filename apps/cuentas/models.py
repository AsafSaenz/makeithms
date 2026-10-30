from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.core.models import TimeStampedModel


class Empresa(TimeStampedModel):
    nombre = models.CharField(max_length=200)
    rfc = models.CharField("RFC", max_length=13, blank=True)
    es_administradora = models.BooleanField(
        default=False, help_text="Marca a Make It HMS, la empresa que administra la plataforma."
    )
    limite_usuarios = models.PositiveIntegerField(null=True, blank=True)
    activa = models.BooleanField(default=True)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Usuario(AbstractUser):
    class Rol(models.TextChoices):
        ADMIN = "admin", "Administrador"
        AUDITOR = "auditor", "Auditor"
        CLIENTE = "cliente", "Cliente"

    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True, blank=True, related_name="usuarios")
    rol = models.CharField(max_length=10, choices=Rol.choices, default=Rol.CLIENTE)
    telefono = models.CharField(max_length=20, blank=True)


class Proyecto(TimeStampedModel):
    class Estatus(models.TextChoices):
        ACTIVO = "activo", "Activo"
        PAUSADO = "pausado", "Pausado"
        CERRADO = "cerrado", "Cerrado"

    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, related_name="proyectos")
    nombre = models.CharField(max_length=200)
    area_geografica = models.CharField(max_length=120, blank=True)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)
    estatus = models.CharField(max_length=10, choices=Estatus.choices, default=Estatus.ACTIVO)
    miembros = models.ManyToManyField(Usuario, through="ProyectoUsuario", related_name="proyectos")

    class Meta:
        ordering = ["empresa__nombre", "nombre"]

    def __str__(self):
        return f"{self.empresa} · {self.nombre}"


class Seccion(models.TextChoices):
    AUDITORIA = "auditoria", "Auditoría"
    QAQC = "qaqc", "QAQC"
    SEGURIDAD_MA = "seguridad_ma", "Seguridad y MA"
    PERSONAL = "personal", "Personal"


class ProyectoUsuario(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    secciones = models.JSONField(default=list, blank=True, help_text="Lista de secciones permitidas.")

    class Meta:
        unique_together = [("proyecto", "usuario")]
        verbose_name = "acceso a proyecto"
        verbose_name_plural = "accesos a proyectos"

    def puede_ver(self, seccion):
        return seccion in self.secciones
