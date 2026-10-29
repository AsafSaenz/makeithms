from django.contrib import admin

from .models import SolicitudCotizacion


@admin.register(SolicitudCotizacion)
class SolicitudCotizacionAdmin(admin.ModelAdmin):
    list_display = ["empresa", "nombre", "correo", "servicio", "estatus", "creado"]
    list_filter = ["estatus", "servicio"]
    search_fields = ["empresa", "nombre", "correo"]
    list_editable = ["estatus"]
