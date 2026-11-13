# Implementar mi propio ecosistema con ChatGPT

**Este es el enlace que debes pasar a tu ChatGPT para comenzar a implementar tu propio sistema de trabajo:**

https://github.com/germaquintana/ecosistemas-gpt-github/blob/main/IMPLEMENTAR_CON_CHATGPT.md

> **Importante:** pegar un enlace por sí solo no instala ni configura nada. Pégalo acompañado de la instrucción de inicio que se indica a continuación. ChatGPT deberá leer esta página, adaptar la guía a tu realidad y ejecutar únicamente las acciones para las que tenga herramientas y permiso. No es una suscripción, instalación automática, política institucional ni cesión de acceso al autor de esta biblioteca.

## 1. Mensaje de arranque — copiar y pegar en tu ChatGPT

```text
Quiero implementar MI PROPIO ecosistema de trabajo con ChatGPT + GitHub y, cuando aporte valor, herramientas complementarias.

Lee primero esta guía pública de implementación:
https://github.com/germaquintana/ecosistemas-gpt-github/blob/main/IMPLEMENTAR_CON_CHATGPT.md

Sigue sus fases e instrucciones, apoyándote en README.md, CONFIGURACIONES_Y_COMPROMISOS.md, docs/ y plantilla-proyecto/ del mismo repositorio.

Primero muéstrame un esquema simple de cómo funcionará, qué buenas prácticas adoptaría, cuáles son opcionales y qué permisos se requerirían. Después guíame para implementarlo de verdad en MI cuenta y repositorio, respetando mis decisiones y usando las herramientas que tengas disponibles.

No copies información privada del autor de esta guía. No hagas cambios en cuentas o repositorios de terceros. Antes de crear, escribir, conectar o publicar, identifica el destino y solicita mi autorización explícita. Si falta una conexión o una capacidad, indícame el paso mínimo que debo hacer y continúa con lo que sí puedas realizar. No afirmes que algo se instaló o escribió sin comprobarlo.

Quiero que el proceso termine con un proyecto propio funcional, su README, AGENTS.md, estado recuperable, una primera tarea verificable, un registro de cambios y una explicación de cómo seguir usando el sistema.
```

## Si quieres mantenerlo actualizado semanalmente

Una vez instalado y verificado tu proyecto, considera la [guía opcional de revisión semanal](plantilla-proyecto/REVISION_SEMANAL_GUIA.md). Ofrece una revisión manual, una tarea recurrente configurada en tu propio asistente o un workflow de GitHub Actions que solo propone una Issue cuando hay diferencias de versión. Ninguna modalidad debe adoptarse sin verificar permisos; **nunca aplica cambios automáticamente**. La [versión pública vigente](VERSION.json) y [el historial](CHANGELOG.md) son la referencia.

## Si ya tienes tu propio sistema: actualización del 13/11/2026

**No lo reconstruyas ni crees otro repositorio.** Consulta [ACTUALIZACION_2026-11-13.md](ACTUALIZACION_2026-11-13.md), que incluye un mensaje listo para copiar para:

- aceptar comentarios normales **o** cambios de checklist como señales, cuando haya una integración autorizada;
- dejar en espera una tarea que requiera decisión humana sin detener los demás trabajos;
- distinguir `run_lock` técnico de la situación de una tarea y tratar bloqueos ajenos con prudencia;
- aplicar control de versiones, IDs de evento e idempotencia;
- probar el circuito realmente, sin declarar funcionamiento por el solo cambio de instrucciones.

La adopción es opcional. Tu asistente debe leer los archivos vigentes y pedir autorización para modificar su destino, sin publicar datos privados ni reproducir configuraciones ajenas.

## 2. Qué debe hacer tu asistente, en orden

### Fase A — Explicar antes de actuar

Lee directamente esta guía y los documentos pertinentes de este repositorio, no solo su nombre. Presenta:

- Un esquema **Persona → Asistente → GitHub → Fuentes y complementos → Verificación humana**.
- Las siete prácticas: objetivo verificable; una autoridad por tipo de dato; instrucciones y estado; tareas sin duplicados; permisos y privacidad; autonomía limitada; control de calidad con evidencia.
- Distinción entre **base recomendada**, **complementos opcionales** y **operaciones que requieren autorización**.
- Breve mapa de lo que se va a construir en la cuenta **del colega**, sin tratar esta guía como sistema operativo común.

Si un archivo no se puede abrir, explica la limitación y no inventes su contenido.

### Fase B — Diagnóstico mínimo y elección de destino

Pregunta por el **tipo de proyecto o área de trabajo** que la persona desea organizar. Después verifica si tiene cuenta GitHub y si **ya posee un repositorio** para ese proyecto. Reutiliza uno existente cuando corresponda y se autorice; evita duplicar repositorios, carpetas y tareas.

No solicites contraseñas, tokens ni archivos internos en el chat. No presupongas que GitHub u otras apps están conectadas. Si el asistente no puede escribir en GitHub, indica cómo conectar una integración disponible mediante las opciones de ChatGPT y cómo comprobar el acceso. **Conectar una integración siempre requiere acción explícita del titular.**

Si la herramienta disponible no puede crear repositorios, explica cómo abrir https://github.com/new y crear un repositorio privado inicialmente. Pide la URL del repositorio resultante y continúa. No inventes un repositorio ni un enlace de éxito.

### Fase C — Preparar el contrato de trabajo

Revisa el proyecto existente antes de escribir. Adapta, no copies a ciegas, los ejemplos de `plantilla-proyecto/`:

- `README.md`: propósito, acceso, guía para retomar.
- `PROYECTO.md`: objetivo, alcance, resultado, responsables, riesgos y criterios de aceptación.
- `AGENTS.md`: reglas y límites del asistente, fuentes y autorizaciones.
- `estado_proyecto.json`: estado verificable, fase, responsable, próxima acción y registro de bloqueo si aplica.
- Una primera tarea/issue con entregable, fechas acreditadas y evidencia exigida.
- Bitácora o RUN de la implementación inicial.

Distingue hechos verificados, propuestas y decisiones pendientes. No reemplaces archivos ni reglas existentes sin revisar los originales y obtener autorización para la modificación.

### Fase D — Implementar en el repositorio propio

**Solo después de que la persona apruebe el destino, alcance y escritura**:

1. Crea o actualiza los archivos esenciales en el repositorio autorizado; usa controles de versión/SHA o mecanismos equivalentes cuando existan.
2. Comprueba por lectura de vuelta que los archivos quedaron persistidos y que sus enlaces funcionan.
3. Registra qué se cambió, cuándo, por qué, con qué evidencia y cuál es la siguiente acción.
4. Si faltan herramientas o permisos, entrega los archivos completos preparados para copiar, sin afirmar que ya están en GitHub.
5. No envíes correos, crees eventos, actives automatizaciones, cambies visibilidad/permisos, ni publiques documentos sin una autorización **independiente y específica**.

La primera iteración puede ser solo el núcleo ChatGPT + GitHub. No hace falta conectar todas las herramientas para que el proyecto funcione.

### Fase E — Complementos modulares, solo cuando se justifiquen

Evalúa Drive u otro almacén documental, Trello/Issues, Gmail, Calendar, dashboards y automatizaciones según la utilidad real del proyecto. Para cada integración define finalidad, custodio de información, fuente de verdad, datos accesibles, lectura/escritura, alcance del permiso, procedimiento de desconexión y evidencia de funcionamiento.

Primero prefiere **solo lectura**; la escritura requiere aprobación separada. No copies expedientes, secretos o datos personales a repositorios públicos. No combines datos de otros usuarios sin finalidad ni permiso legítimos.

### Fase F — Verificar funcionamiento y entregar al colega

Prueba un ciclo pequeño y real: **leer instrucciones y estado → ejecutar una unidad autorizada → comprobar producto → registrar cambio/RUN → dejar próxima acción**.

Termina con:

- Enlace del repositorio propio comprobado (si fue creado o modificado efectivamente).
- Mapa del sistema instalado y herramientas conectadas **verificadas**.
- Resumen de prácticas implementadas, prácticas pendientes y autorizaciones aún necesarias.
- Primera tarea, responsable y criterio de cierre.
- Instrucción corta que el colega pueda pegar en una conversación posterior para recuperar su proyecto desde GitHub.

No confundas prueba sintética con operación real, ni documento generado con documento aprobado o publicado.

## 3. Lo que esta guía NO autoriza

La URL no concede acceso al GitHub del autor ni a cuentas del colega; no crea cuentas ni suscripciones; no activa tareas programadas; no da acceso a Gmail, Drive u otros complementos; no habilita publicaciones ni cambios de permisos; no impone normas municipales a proyectos particulares.

**Para organizaciones e instituciones:** quien use la guía debe adaptar sus responsabilidades, políticas de datos, procedimientos y aprobación. No asumir que las instrucciones genéricas sustituyen las reglas de su empleador.

## 4. Si tu ChatGPT no puede acceder al repositorio

Pega el texto de esta guía en el chat o comparte los archivos descargados. Pide que prepare el paquete para instalarlo manualmente o que te oriente para conectar GitHub, si tienes acceso legítimo y decides hacerlo.

## 5. Dos formas de compartir

**Más simple:** envía a tu colega esta página y dile: «Pega el enlace y el mensaje del apartado 1 en tu ChatGPT».

**Más directo:** envía una sola línea para que la pegue como mensaje en su ChatGPT:

> Implementa en mi propio entorno, paso a paso y con mi autorización para cada cambio, el sistema descrito aquí: https://github.com/germaquintana/ecosistemas-gpt-github/blob/main/IMPLEMENTAR_CON_CHATGPT.md . Comienza por mostrarme un esquema y preguntarme qué proyecto quiero gestionar; después lee la guía y ejecuta sus fases con las herramientas disponibles, sin inventar éxitos ni conectar cuentas sin consentimiento.

El **único enlace no basta** para obligar a ChatGPT a actuar: debe existir una instrucción en la conversación. El asistente no puede disponer de herramientas que no estén disponibles en la cuenta del colega.
