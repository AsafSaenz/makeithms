from django.conf import settings
from django.core.mail import mail_admins
from django.shortcuts import render

from .forms import SolicitudCotizacionForm


def inicio(request):
    return render(request, "landing/index.html", {"form": SolicitudCotizacionForm()})


def cotizar(request):
    """Recibe el formulario por HTMX y devuelve solo el bloque del formulario."""
    form = SolicitudCotizacionForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        solicitud = form.save()
        if settings.ADMINS:
            mail_admins(f"Nueva cotización: {solicitud}", f"{solicitud.nombre} <{solicitud.correo}>\n\n{solicitud.mensaje}")
        return render(request, "landing/_cotizacion_enviada.html")
    return render(request, "landing/_form_cotizacion.html", {"form": form})
