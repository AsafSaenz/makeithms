# Requisitos confirmados con Hugo (29/10/2026)

Contacto: Ing. Hugo Montemayor, +52 81 2200 3118, México.

## Alcance
| Tema | Respuesta |
| --- | --- |
| Usuarios | Clientes (empresas) que ingresan solos con su usuario y registran todo en la herramienta |
| Modelo de negocio | Plataforma vendida **por usuario**, en paquetes de 5, 10, etc. |
| Segunda etapa | Cumplimiento legal y un par de módulos más (por definir). **Decisión 05/11/2026: todo entra en la primera fase** |
| Control documental | Hugo entregará una carpeta con la estructura que los clientes usarán para cargar documentos |
| Personal | Incluye competencia (capacitaciones, expedientes) |

## Operación
| Tema | Respuesta |
| --- | --- |
| Normas | Las ISO (9001, 14001, 45001); las NOM entran dentro de seguridad |
| Formatos | Hugo los prepara: listas de verificación, reporte de auditoría, reporte de hallazgos y NCR |
| Calificación | Por aclarar: Hugo preguntó "¿cómo?" |
| Respuestas del cliente | No hay llenado previo a la visita; se contesta durante el proceso de auditoría |
| ITP | Sí, con puntos Hold y Witness; vienen en los propios ITP |
| Área geográfica | Puede ser sitio, región o país |

## Marca
- MS = Management System.
- Dominio: Hugo tenía makeithms.com; falta confirmar si se puede reactivar.

## Respuestas del 05/11/2026
| Tema | Respuesta |
| --- | --- |
| RDA | Reporte de Deficiencia de Auditoría |
| RDP | Reporte de Deficiencia Potencial |
| Calificación de auditorías | No hay puntaje. El estatus es: planeada, en proceso, cerrada o cancelada |
| Listas de verificación | Muchas veces se arman específicas para lo que se audita; Hugo enviará dos ejemplos |
| ITP | Hugo enviará un ejemplo lleno y uno vacío |
| Estructura documental | Hugo la enviará |
| Punch list e inspecciones | Se capturan en la plataforma; deben poder exportarse a Excel |
| Programa de inspecciones | Entra en la primera etapa si es posible. Se programa por área (ej. Laminación) o por equipo (ej. Motor #…) |

## Material recibido (05/11/2026)
Formatos de auditoría interna (notificación, lista de verificación vacía, asistencia, informe, reporte de deficiencia), programa de inspecciones con dashboard, reporte fotográfico, informe de inspección de material y un punch list. Contienen datos reales del cliente y no se guardan en este repo.

## Material recibido el 05/11/2026 (segundo envío)
- **Lista de verificación ISO 9001:2015** (Excel). Hugo la actualizará a la versión 2026. Las listas por proceso las desarrolla el auditor líder.
  - Columnas: cláusula, requisito, cumplimiento y observaciones.
  - Cada requisito se responde: Sí cumple (2), En proceso (1), No cumple (0) o No aplica (no cuenta).
  - Calcula el porcentaje de cumplimiento por cláusula (puntos entre 2 por requisito aplicable) y un cumplimiento general.
  - Esto no es una calificación de la auditoría. El estatus de la auditoría sigue siendo planeada, en proceso, cerrada o cancelada.
- **ITP** (Plan de Inspección y Pruebas) de montaje de estructuras metálicas. Cada actividad tiene requisito, documento de referencia, registro y códigos por responsable (contratista, supervisión y cliente).
  - Códigos: W testificar, H punto de espera, R revisión de registro, I inspección, E ejecutar, M monitorear, V verificar, A aceptar.
  - Un responsable puede tener varios códigos en la misma actividad (por ejemplo H e I).
- **Estructura documental del SIG** (Sistema Integrado de Gestión): carpetas 00 Gobierno del Sistema, 01 Liderazgo, 02 Información Documentada y 03 Gestión de Riesgos. El mensaje llegó cortado en la carpeta 03 (terminaba en "Plan…"). Hugo aclara que esa estructura es por norma y que el usuario debe poder crear carpetas propias, más bien por proceso.

## Implicaciones para el diseño
- Cobro por usuario: necesitamos un límite de usuarios activos por `Empresa` (tope del paquete).
- `quien_responde = Cliente` ya no implica llenado previo: el cliente responde durante la auditoría.
- Área geográfica: modelo flexible (sitio / región / país).

- Respuesta de la pregunta por pregunta: cuatro valores (sí cumple, en proceso, no cumple, no aplica) en lugar de sí / no / N.A.
- ITP: los puntos de inspección se guardan por responsable y pueden ser varios por actividad, no una sola letra.
- Documentos: carpetas base del SIG más carpetas creadas por el usuario.

## Pendientes
- Pedir a Hugo el resto de la estructura documental (a partir de la carpeta 03).
- Recibir de Hugo la estructura documental y los ejemplos de ITP (lleno y vacío) y de listas de verificación.
- Definir cuáles son los "par de módulos más" que acompañan a Cumplimiento legal (ahora también en la primera fase).
- Confirmar la reactivación del dominio makeithms.com.
