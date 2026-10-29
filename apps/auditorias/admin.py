from django.contrib import admin

from .models import Auditoria, Plantilla, Pregunta, Respuesta


class PreguntaInline(admin.TabularInline):
    model = Pregunta
    extra = 3
    fields = ["orden", "apartado", "texto", "tipo", "quien_responde", "punto_inspeccion", "requiere_evidencia", "peso"]


@admin.register(Plantilla)
class PlantillaAdmin(admin.ModelAdmin):
    list_display = ["nombre", "norma", "seccion", "version", "activa"]
    list_filter = ["seccion", "activa"]
    search_fields = ["nombre", "norma"]
    inlines = [PreguntaInline]


class RespuestaInline(admin.TabularInline):
    model = Respuesta
    extra = 0
    fields = ["pregunta_id_original", "valor_cliente", "valor_auditor", "estatus"]


@admin.register(Auditoria)
class AuditoriaAdmin(admin.ModelAdmin):
    list_display = ["titulo", "empresa", "proyecto", "auditor", "fecha_programada", "estatus"]
    list_filter = ["estatus", "empresa"]
    search_fields = ["titulo"]
    readonly_fields = ["token_cliente"]
    inlines = [RespuestaInline]

    def save_model(self, request, obj, form, change):
        if not obj.preguntas_congeladas:
            obj.congelar_preguntas()
        super().save_model(request, obj, form, change)
