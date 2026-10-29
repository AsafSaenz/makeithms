from django import forms

from .models import SolicitudCotizacion


class SolicitudCotizacionForm(forms.ModelForm):
    class Meta:
        model = SolicitudCotizacion
        fields = ["nombre", "empresa", "correo", "telefono", "servicio", "mensaje"]
        labels = {"mensaje": "¿Qué necesitas revisar?", "servicio": "Servicio de interés"}
        widgets = {"mensaje": forms.Textarea(attrs={"rows": 4})}
