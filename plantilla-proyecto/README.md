# Plantilla mínima para tu propio proyecto GPT + GitHub

Copia estos archivos a **tu repositorio nuevo y privado** y adapta las instrucciones. No confíes en los ejemplos como reglas oficiales de una organización.

| Archivo | Uso |
|---|---|
| [PROYECTO.md](PROYECTO.md) | Problema, objetivo, resultados, alcance y destinatario |
| [AGENTS.md](AGENTS.md) | Instrucciones y límites para el asistente |
| [estado_proyecto.json](estado_proyecto.json) | Estado resumido, bloqueo y próxima unidad |
| [REGISTRO_MODULOS.json](REGISTRO_MODULOS.json) | Complementos candidatos y su autorización |
| [plantillas/TAREA.md](plantillas/TAREA.md) | Definición de un entregable |
| [bitacora/EJEMPLO_RUN.md](bitacora/EJEMPLO_RUN.md) | Registro mínimo de una ejecución |

**Primero:** cambia los nombres y objetivos de ejemplo, el responsable y las reglas de seguridad según tu caso. No copies datos de trabajo reales hasta comprobar acceso y finalidad.

**Después:** pide al asistente que lea `AGENTS.md` y `estado_proyecto.json`, resuma su próximo paso y **proponga** su primera tarea sin ejecutar cambios. Puedes usar [el prompt principal de evaluación](../PROMPT_PARA_CHATGPT.md) antes de crear nada.

La plantilla **no concede acceso** a GitHub, correo, Drive, calendarios ni servicios externos. Tampoco instala tareas programadas.
