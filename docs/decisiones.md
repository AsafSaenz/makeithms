# Decisiones del proyecto

Plan completo: https://claude.ai/artifact/5bMceGY6qsekgoRFWYuc6r

| Tema | Decisión | Por qué |
| --- | --- | --- |
| Framework | Django 5.2 + PostgreSQL | Admin, auth, permisos y búsqueda full-text listos; un solo desarrollador entrega rápido |
| Front | HTMX + Alpine.js + Tailwind, renderizado en servidor | Un solo código, responsivo, sin SPA |
| Multiempresa | Un esquema, FK `empresa` en cada modelo (`EmpresaModel`), filtro explícito `.para(empresa)` | Simple de operar y revisar |
| Usuario | Modelo propio `cuentas.Usuario` desde la primera migración | Cambiarlo después es muy costoso |
| Seguimiento | Una entidad `Asunto` para hallazgos, NCR, observaciones, incidentes, accidentes y riesgos | Un solo tablero en lugar de cinco módulos |
| Plantillas | Cada pregunta tiene `quien_responde` (Cliente, Auditor, Ambos) y `punto_inspeccion` (H, W, R) | Reparte el trabajo y soporta ITP de obra |
| Auditoría | Copia congelada de preguntas al crearla | Editar la plantilla no altera auditorías en curso |
| Respuestas | Se guarda la respuesta del cliente y la corrección del auditor por separado | Trazabilidad |
| Documentos | `tsvector` + GIN para contenido, JSONB para metadatos, estados WIP/compartido/publicado/archivado | Sin Elasticsearch; alineado a ISO 19650 |
| Tareas | django-q2 sobre la misma base | Sin Redis ni worker de pago |
| Archivos | Cloudflare R2 vía django-storages | Barato y sin cobro de egreso |
| Correo | Resend por SMTP | Plan gratis para arrancar |
| Hosting | Render (web + Postgres) | Cero administración de servidor |
| PDF | WeasyPrint | Reportes con el CSS de la marca |

## Pendiente de confirmar con Hugo
Ver la sección de preguntas del plan.
