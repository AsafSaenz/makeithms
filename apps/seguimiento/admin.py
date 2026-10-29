from django.contrib import admin

from .models import Asunto, Evidencia


class EvidenciaInline(admin.TabularInline):
    model = Evidencia
    fk_name = "asunto"
    extra = 1
    fields = ["archivo", "descripcion"]


@admin.register(Asunto)
class AsuntoAdmin(admin.ModelAdmin):
    list_display = ["titulo", "proyecto", "origen", "tipo", "severidad", "responsable", "fecha_limite", "estatus"]
    list_filter = ["estatus", "origen", "tipo", "severidad", "empresa"]
    search_fields = ["titulo", "descripcion"]
    inlines = [EvidenciaInline]
