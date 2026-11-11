# 02 · Arquitectura de un ecosistema personal

| Capa | Función | Ejemplo | Límite |
|---|---|---|---|
| Persona | Autoriza y acepta resultados | Define qué se publica | No delegar decisiones reservadas |
| GPT o asistente | Ayuda con análisis y ejecución permitida | Redacta y comprueba borradores | No asumir que sabe el estado actual |
| GitHub | Trabajo versionado | README, AGENTS, issues, RUN, código | No reemplaza sistemas originales |
| Fuente documental | Datos y versiones originales | Drive, SharePoint, archivos locales | Acceso y derechos vigentes |
| Complementos | Comunicaciones, seguimiento, hitos | Gmail, Trello, Calendar | Solo cuando son útiles y autorizados |

**Fuente de verdad por tipo de dato:** GitHub para decisiones y estado de proyecto, correo para el mensaje que efectivamente se envió, Drive para el original archivado y sistema externo para el trámite confirmado. Una interfaz derivada no sustituye la prueba original.

El mínimo adecuado depende del proyecto. Un ejercicio puede funcionar con asistente + GitHub; un proyecto con documentos necesita almacenamiento y controles de acceso. Evita crear herramientas duplicadas.

## Interoperabilidad por referencias
Conserva URLs/IDs y fechas, no copias indiscriminadas de documentos. Los cambios entre módulos deben ser explícitos, limitados y verificables. Nunca asumas que una integración técnica significa autorización para operar sobre una organización ajena.
