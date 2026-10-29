from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

admin.site.site_header = "Make It MS"
admin.site.site_title = "Make It MS"
admin.site.index_title = "Administración"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.landing.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
