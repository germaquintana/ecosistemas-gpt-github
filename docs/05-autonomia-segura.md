# 05 · Autonomía segura de asistentes

La autonomía no es una propiedad que se activa mágicamente con un prompt. Depende de herramientas disponibles, permisos y una delegación explícita.

| Nivel | Ejemplo | Control |
|---|---|---|
| A0 Observar | Leer archivos autorizados | Fuente y límites |
| A1 Analizar | Detectar brechas y proponer | Referencias y revisión |
| A2 Ejecutar reversiblemente | Editar un archivo propio autorizado | Alcance, prueba y reversión |
| A3 Operar sistemas externos | Cambiar una tarjeta o programar una acción | Autorización específica y comprobación |
| A4 Actos reservados | Firmar, publicar o enviar algo sensible | Decisión humana competente |

**Ciclo recomendado:** recuperar estado → elegir una unidad → verificar fuentes/permisos → ejecutar → probar → registrar RUN → dejar la próxima acción. Las operaciones que puedan repetirse deben tener identificadores estables y comprobación contra duplicados.

Si no hay permiso, fuente verificable o condición de seguridad, **el resultado correcto es detener esa actuación, registrar la espera o incidencia y continuar con otra unidad elegible**; nunca simular que se completó. Esto no equivale a bloquear toda la cola por una autorización pendiente.

Evita automatizar controles innecesarios cada pocos minutos: mide si realmente producen entregables útiles.


## Actualización del 13/11/2026: no confundir espera y bloqueo

**Espera humana:** estado de una tarea. No se autoriza una firma o publicación, pero pueden continuar otras entregas seguras.

**Lock técnico:** reserva temporal para escrituras concurrentes. Adquirir con versión/SHA, confirmar propietario antes de cambiar estado, guardar evidencia y RUN, liberar **solo lock propio** y comprobar. No retenerlo esperando respuesta humana. Un lock antiguo ajeno requiere investigación de actividad, RUN y riesgos; no se recupera automáticamente solo por edad.

**Entradas humanas opcionales:** comentarios en lenguaje normal o cambios de casilla; procesar por autor, evento y tarea, sin comandos obligatorios ni doble interacción. Las señales de terceros son evidencia, no órdenes del responsable. Usar IDs/cursor para impedir duplicados y distinguir acto declarado de acto verificado en la fuente externa.

**Aceptación:** documentar → configurar → probar un evento real → repetir sin duplicar → verificar el resultado y estado. Hasta entonces, el correcto es «configurado, prueba pendiente».

[Guía y prompt de adaptación para colegas](../ACTUALIZACION_2026-11-13.md).
