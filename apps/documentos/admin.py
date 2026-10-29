from django.contrib import admin

from .models import Documento


@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ["titulo", "codigo", "revision", "estado", "proyecto", "seccion"]
    list_filter = ["estado", "seccion", "empresa"]
    search_fields = ["titulo", "codigo"]
