# Make It HMS

Plataforma QHSE de Make It HMS: auditorías con cuestionarios para cliente y auditor, seguimiento de hallazgos, control documental y landing con solicitudes de cotización.

*Make it good. Make it safe. Make it green.*

## Stack
Django 5.2 · PostgreSQL · HTMX + Alpine.js + Tailwind · django-q2 · Cloudflare R2 · Resend · Render.
Decisiones y razones en [`docs/decisiones.md`](docs/decisiones.md).

## Arranque local

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env            # ajusta DATABASE_URL

# PostgreSQL con Docker (opcional)
docker run -d --name makeithms-db -p 5432:5432 \
  -e POSTGRES_USER=makeithms -e POSTGRES_PASSWORD=makeithms -e POSTGRES_DB=makeithms postgres:16

python manage.py makemigrations cuentas auditorias seguimiento documentos landing
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

- Landing: http://localhost:8000
- Admin: http://localhost:8000/admin

Las migraciones iniciales no vienen en el repo: genéralas con el comando de arriba y súbelas en el siguiente commit.

## Estructura

```
config/            settings, urls, wsgi
apps/core          modelos base (TimeStamped, EmpresaModel) y middleware de empresa
apps/cuentas       Empresa, Usuario (propio), Proyecto, accesos por sección
apps/auditorias    Plantilla, Pregunta (quién responde, punto H/W/R), Auditoría, Respuesta
apps/seguimiento   Asunto (hallazgo, NCR, observación, incidente, riesgo) y Evidencia
apps/documentos    Documento con búsqueda full-text y metadatos (fase 2)
apps/landing       Sitio público y solicitudes de cotización (HTMX)
templates/         base, escudo SVG de la marca, landing
```

## Despliegue
`render.yaml` crea el servicio web y la base PostgreSQL en Render. Variables de R2 y Resend se capturan en el panel.

## Siguientes pasos
1. Generar migraciones y cargar una plantilla real de Hugo.
2. Liga del cliente (`/c/<token>/`) para contestar sus preguntas.
3. Vista del auditor en celular.
4. Tablero de seguimiento y reporte PDF.
