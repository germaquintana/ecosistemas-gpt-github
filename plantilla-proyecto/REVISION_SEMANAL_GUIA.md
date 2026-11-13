# Revisión semanal de novedades de la guía — instalación opcional

**Guía de referencia:** https://github.com/germaquintana/ecosistemas-gpt-github  
**Fecha del patrón:** 13/11/2026. Este mecanismo **no se instala por abrir el enlace**.

## Opción más simple: revisión asistida

Si ya utilizas un asistente con acceso a tu proyecto, puedes darle esta instrucción **una vez** en la tarea de revisión periódica que tú elijas, sin crear integraciones adicionales:

> Una vez por semana, consulta https://github.com/germaquintana/ecosistemas-gpt-github/blob/main/VERSION.json y compara con mi `version_guia_adoptada.json`. Si hay una versión distinta, lee CHANGELOG y las notas, analiza qué criterios son pertinentes a mi proyecto y deja una propuesta con riesgos, permisos y prueba de aceptación. No cambies mis archivos, conectores, autorizaciones ni automatizaciones sin mi aprobación. Si no hay cambios, no crees tareas ni informes redundantes. Nunca declares aplicada una versión sin verificarla.

**Importante:** el asistente solo cumplirá ese horario si realmente cuenta con una automatización habilitada en tu entorno. Un texto en `AGENTS.md` no programa nada por sí mismo.

## Opción GitHub Actions: aviso por Issue

Esta biblioteca incluye un [ejemplo de workflow](automatizaciones/revisar_novedades_semanal.yml). Está guardado fuera de `.github/workflows` **para que no se active al copiar la plantilla**.

Pasos para un proyecto propio, cuando tengas acceso de escritura y quieras recibir avisos:

1. Configura o adapta `version_guia_adoptada.json` **en la raíz de tu propio repositorio**. La versión debe representar la guía efectivamente adoptada, no la última que encontraste en internet.
2. Lee el código del workflow de ejemplo y acepta su alcance; luego **cópialo** a `.github/workflows/revisar-novedades-ecosistema.yml` en tu propio repositorio.
3. Si quieres que abra una Issue con las novedades, GitHub Actions deberá poder escribir Issues mediante `GITHUB_TOKEN` con alcance `issues: write`; no necesita un token personal del autor. Si no se habilita, documenta la limitación.
4. Comprueba el primer `workflow_dispatch` manual y observa la ejecución antes de depender de la programación semanal.
5. Cuando adoptes una versión, documenta cambios, permisos, pruebas y RUN; **actualiza manualmente** `version_guia_adoptada.json` para reflejar lo que realmente funciona.

**Comportamiento previsto:** consulta semanal del manifiesto público; si versión distinta, abre a lo sumo una Issue abierta con título estable para esa versión; si es igual, no hace nada. Nunca aplica cambios ni envía comunicaciones.

## Alternativa sin automatizaciones

Abre una vez por semana [VERSION.json](../VERSION.json) y [CHANGELOG.md](../CHANGELOG.md), revisa las diferencias y solicita una propuesta de adaptación a tu asistente. Este enfoque es suficiente para proyectos pequeños.

## Límites

- La guía no te incorpora automáticamente a una red ni comparte tus datos con otros proyectos.
- GitHub puede retrasar ejecuciones programadas o deshabilitarlas tras inactividad; comprueba la pestaña Actions.
- Las Issues del repositorio consumidor pueden ser visibles para quienes tengan acceso a él: no incluyas información privada en el aviso.
- La licencia del material público sigue su propio estado; no presupongas libre redistribución de cualquier archivo.
