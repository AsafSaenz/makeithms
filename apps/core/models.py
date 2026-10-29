"""Modelos base compartidos.

Multiempresa: un solo esquema. Todo modelo de negocio hereda de
`EmpresaModel` y se consulta con `.para(empresa)`. El filtro es explícito
a propósito: es más fácil de revisar que un filtro mágico por hilo.
"""

from django.db import models


class TimeStampedModel(models.Model):
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class EmpresaQuerySet(models.QuerySet):
    def para(self, empresa):
        return self.filter(empresa=empresa)


class EmpresaModel(TimeStampedModel):
    empresa = models.ForeignKey("cuentas.Empresa", on_delete=models.PROTECT, related_name="+")

    objects = EmpresaQuerySet.as_manager()

    class Meta:
        abstract = True
