# Actualización 13/11/2026 — versión 1.2.0: mejora continua semanal

**Publicación editorial:** 13 de noviembre de 2026. **Ámbito:** guía pública para colegas; adopción voluntaria.

Esta versión añade un **mecanismo permanente de consulta y mejora** al modelo de trabajo descrito en la [actualización v1.1](ACTUALIZACION_2026-11-13.md).

## Qué cambia

- **Versión central consultable:** [VERSION.json](VERSION.json) distingue la última versión publicada del sistema de cada colega. Se complementa con [CHANGELOG.md](CHANGELOG.md), por fecha y criterios de aceptación.
- **Revisión editorial semanal del origen:** un flujo de GitHub Actions programado los **lunes 09:17 (America/Santiago)** comprueba la coherencia documental y muestra hallazgos en el resumen de la ejecución; es **solo lectura**, no publica actualizaciones ni reemplaza a una persona que evalúe mejoras reales.
- **Actualización voluntaria de colegas:** una guía de [revisión semanal](plantilla-proyecto/REVISION_SEMANAL_GUIA.md) y un workflow de ejemplo permiten detectar diferencias en el repositorio propio. Si se instala y autoriza expresamente, puede crear **una Issue de revisión por versión**, no aplicar modificaciones.
- **Separación clara de versiones:** `VERSION.json` del origen refleja lo publicado; `version_guia_adoptada.json` del colega refleja cambios **realmente incorporados y probados**, sin adelantar el número por una simple lectura.
- **Continuidad y calidad:** si no hay novedades, no se generan trabajos repetitivos. Si hay novedades, se comparan, se deciden, se prueban y se registran como cambios propios. Las aprobaciones de envío, publicación, firmas y datos sensibles siguen siendo humanas.

## Cómo seguir la guía sin programar nada

Puedes revisar una vez a la semana:
1. [Versión publicada](VERSION.json).
2. [Historial](CHANGELOG.md).
3. [Mejora continua semanal](docs/MEJORA_CONTINUA_SEMANAL.md).

Si tienes un asistente con tareas programadas, puedes **autorizarle** una consulta semanal de estas tres fuentes en su propia cuenta. El texto de la guía no crea por sí solo una tarea programada.

## Cómo instalar la revisión automática en tu propio proyecto

Usa la [plantilla de adopción](plantilla-proyecto/REVISION_SEMANAL_GUIA.md). Está preparada para **no activarse automáticamente** al leer este repositorio. Requiere configurar tu versión adoptada, revisar permisos y habilitar conscientemente el workflow en tu propia cuenta. La prueba de la primera ejecución todavía corresponde a cada titular.

## Criterios de aceptación

- En el origen: `VERSION.json` y `CHANGELOG.md` coherentes; ejecución real y resumen semanal comprobados (no basta un archivo YAML).
- En el proyecto consumidor: versión diferente detectada, una Issue de revisión no duplicada, sin cambios automáticos a la configuración local.
- Al adoptar: autorización humana, análisis de diferencias, pruebas, RUN y actualización del marcador de adopción.
- En caso de error: informar ausencia de conexión, permiso insuficiente o prueba faltante, sin afirmar que la revisión tuvo lugar.

**Estado al publicar:** archivos y programación preparados en GitHub; **primera ejecución programada y prueba extremo a extremo aún pendientes**. La guía no certifica integraciones externas ni se convierte en política oficial de ninguna institución.
