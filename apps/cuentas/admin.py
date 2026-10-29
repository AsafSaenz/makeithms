from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Empresa, Proyecto, ProyectoUsuario, Usuario


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ["nombre", "rfc", "es_administradora", "activa"]
    search_fields = ["nombre", "rfc"]
    list_filter = ["activa"]


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    list_display = ["username", "email", "empresa", "rol", "is_active"]
    list_filter = ["rol", "empresa", "is_active"]
    fieldsets = UserAdmin.fieldsets + (("Make It MS", {"fields": ("empresa", "rol", "telefono")}),)


class ProyectoUsuarioInline(admin.TabularInline):
    model = ProyectoUsuario
    extra = 1


@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "empresa", "area_geografica", "estatus"]
    list_filter = ["estatus", "empresa"]
    search_fields = ["nombre"]
    inlines = [ProyectoUsuarioInline]
