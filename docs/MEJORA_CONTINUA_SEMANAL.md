# Mejora continua semanal del ecosistema GPT + GitHub

**Versión del procedimiento:** 1.0 · **Adoptado como recomendación:** 13/11/2026.
**Ámbito:** repositorio público formativo y proyectos propios que opten por seguirlo.
**No es una política institucional, una instalación automática ni una autorización para modificar repositorios ajenos.**

## 1. Dos circuitos independientes

### A. Revisión editorial del repositorio de referencia

Cada **lunes a las 09:17 America/Santiago** se recomienda un control de calidad y novedades del repositorio de guía. El archivo [workflow de revisión editorial](../.github/workflows/revision-editorial-semanal.yml) puede realizar comprobaciones **solo de lectura** y dejar un resumen visible en GitHub Actions. No produce contenido, no escribe repositorios, no crea Issues y no revisa semánticamente nuevos aprendizajes por sí mismo.

La revisión **humana o asistida** del responsable debe:
1. Contrastar [CHANGELOG.md](../CHANGELOG.md), [VERSION.json](../VERSION.json) y la documentación vigente.
2. Identificar aprendizajes reales, propuestas de Issues, problemas de adopción y nuevas necesidades.
3. Descartar duplicados y diferenciar correcciones menores de cambios de criterios.
4. Proponer un cambio acotado, probarlo con ejemplos ficticios y comprobar que no revela información privada.
5. Incrementar la versión **solo si hay cambios materiales** y actualizar `CHANGELOG.md`, `VERSION.json`, documentación afectada y fecha de publicación.
6. Registrar evidencia del cambio (commit, pruebas, limitaciones). Si no hay mejora, dejar sin cambio de versión. No generar publicaciones ficticias.

La revisión periódica **no es igual a publicar una nueva versión**. No se garantiza que se ejecute puntualmente: los flujos programados pueden retrasarse o deshabilitarse en repositorios públicos inactivos. Consulta el historial de Actions para confirmar ejecuciones.

### B. Revisión semanal en el proyecto de cada colega

El ecosistema del colega puede comprobar semanalmente el [manifiesto de versión público](../VERSION.json). Guarda localmente qué versión **ha adoptado efectivamente**, sin descargar datos institucionales ni depender de cuentas del autor.

- **Igual:** no crear tarea ni reporte repetido; conservar el control de última consulta en logs de la herramienta.
- **Diferente:** mostrar resumen y enlace a novedades; si el colega habilita la plantilla de GitHub Actions, abrir una **única Issue de revisión** por versión pendiente, sin editar código ni instrucciones.
- **Aplicar:** leer los propios `AGENTS.md`, tareas, estado y permisos; evaluar diferencias; proponer cambios y obtener autorización del titular antes de modificar.
- **Verificar:** ejecutar pruebas en el sistema del colega, registrar RUN, y solo después cambiar su `version_guia_adoptada.json`. El número no es prueba de instalación ni de funcionamiento por sí solo.
- **Fallo de consulta:** no asumir que no hay novedades, ni avanzar versión ni ejecutar acciones externas.

La plantilla [revisión semanal para colegas](../plantilla-proyecto/REVISION_SEMANAL_GUIA.md) incluye una opción manual y un workflow **optativo**, que no se activa hasta que el titular lo instale y autorice.

## 2. Fuente de verdad y campos mínimos

El **origen público** mantiene `VERSION.json`, `CHANGELOG.md` y notas por versión. Cada **proyecto consumidor** mantiene su propio `version_guia_adoptada.json` o equivalente. La fecha de comprobación puede registrarse en el historial de ejecuciones, sin modificar el estado por consultas negativas.

Distinguir:
- `ultima_version_publicada`: información pública observada y verificada;
- `version_adoptada`: decisión del titular y cambios aplicados, **no el resultado de una simple lectura**;
- `propuesta_pendiente`: diagnóstico de diferencias sin permisos para aplicarlas;
- `prueba_aceptacion`: evidencia de funcionamiento, no afirmación del asistente.

## 3. Seguridad y alcance

- **Solo lectura** para consultar publicaciones públicas; no usar tokens personales del autor, ni copiar repositorios privados.
- No instalar workflows, conectores, tareas programadas ni conceder permisos por el solo hecho de abrir la guía.
- No modificar repositorios de colegas por una nueva publicación: obtener autorización y comprobar autoridad sobre cada destino.
- No ejecutar fragmentos de código descargados de un repositorio remoto. El workflow de ejemplo únicamente interpreta JSON público como datos.
- Proteger privacidad, licencias y fuentes originales; los ejemplos son pedagógicos. No confundir la lectura pública con licencia abierta para redistribuir cualquier material.
- Si GitHub Issues están desactivadas o `GITHUB_TOKEN` no puede escribir Issues, informar el límite: no simular aviso entregado.
- Cualquier recomendación puede ser rechazada; un sistema sigue siendo válido aunque conserve una versión anterior, si evalúa conscientemente sus riesgos.

## 4. Indicadores de calidad recomendados

| Indicador | Meta orientativa | Evidencia |
|---|---|---|
| Revisión semanal del origen | Una revisión cada semana calendario | Ejecución GitHub Actions y evaluación humana separadas |
| Actualizaciones detectadas | No perder cambios de versión | Comparación de manifest con adopción local |
| Duplicaciones | Ninguna Issue repetida para la misma versión abierta | ID de Issue o búsqueda por título exacto |
| Aplicación de cambios | Siempre con control de autorizaciones y pruebas | Commit/RUN en proyecto del colega |
| Información privada expuesta | Ninguna | Revisión de contenido y permisos antes de publicar |
| Novedades sin valor real | No subir versión por rutina | Historial consistente |

## 5. Responsabilidades

**Mantenedor de la guía:** revisa propuestas y publica cambios; no controla instalaciones ajenas.

**Colega titular del proyecto:** decide qué versión adoptar, a qué integraciones acceder y qué automatizar.

**Asistente:** analiza diferencias y propone acciones dentro de permisos; no inventa verificaciones ni intervenciones humanas.

## 6. Puesta en marcha

- Para el repositorio de referencia: revisar [GitHub Actions](https://github.com/germaquintana/ecosistemas-gpt-github/actions), comprobar que el workflow editorial está habilitado y observar su primera ejecución real.
- Para el proyecto de un colega: seguir [REVISION_SEMANAL_GUIA.md](../plantilla-proyecto/REVISION_SEMANAL_GUIA.md); el workflow de ejemplo solo se activa después de instalarlo deliberadamente en su repositorio.
- El primer control no reemplaza una auditoría integral; documentar alcance y pendientes. **Una programación guardada no es una ejecución verificada.**
