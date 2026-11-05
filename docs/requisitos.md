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

## Implicaciones para el diseño
- Cobro por usuario: necesitamos un límite de usuarios activos por `Empresa` (tope del paquete).
- `quien_responde = Cliente` ya no implica llenado previo: el cliente responde durante la auditoría.
- Área geográfica: modelo flexible (sitio / región / país).

## Pendientes
- Recibir de Hugo la estructura documental y los ejemplos de ITP (lleno y vacío) y de listas de verificación.
- Definir cuáles son los "par de módulos más" que acompañan a Cumplimiento legal (ahora también en la primera fase).
- Confirmar la reactivación del dominio makeithms.com.
