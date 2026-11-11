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

Si no hay permiso, fuente verificable o condición de seguridad, **el resultado correcto es bloquear o proponer**, no simular que se completó.

Evita automatizar controles innecesarios cada pocos minutos: mide si realmente producen entregables útiles.
