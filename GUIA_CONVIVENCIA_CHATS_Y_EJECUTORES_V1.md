# Convivencia entre chats manuales y ejecutores programados

**Edición pública:** 16-11-2026. Patrón reutilizable; no incluye datos privados ni instrucciones de acceso a sistemas municipales.

## El problema

Un asistente manual puede reservar un repositorio mientras analiza o escribe. Si otro asistente encuentra ese recurso ocupado, no debe asumir que se trata de una avería ni paralizar todos los trabajos.

## Patrón seguro de trabajo federado

1. Una **cola común** conserva referencias a tareas y su fuente de verdad, no copia expedientes ni secretos.
2. Cada candidato informa su repositorio o recurso de origen. Antes de escribir, leer sus instrucciones, permisos, estado y lock.
3. Si otro propietario tiene un lock activo, **omitir ese nodo** y seleccionar otro trabajo independiente en la **misma ejecución**. No liberar el lock ni concluir que está abandonado solo por su edad.
4. Para un candidato libre, reclamar el ítem mediante actualización condicionada por versión/SHA, releer para confirmar, y revisar nuevamente el estado del origen antes de escribir.
5. Al terminar, registrar evidencia del producto, RUN, commit/SHA, estado de entrega y siguiente acción; liberar **solo el propio** lock. Si falla la reconciliación, comprobar producto anterior antes de reintentar para evitar duplicados.
6. Revalidar en el siguiente ciclo los candidatos que estaban ocupados. Un bloqueo observado es temporal y puede desaparecer.
7. Si no hay candidatos independientes, registrar `SIN_TRABAJO_DESBLOQUEADO` sin producir registros vacíos ni inventar resultados.

## Límites importantes

- Un lock en GitHub no permite saber con certeza si una conversación sigue abierta; es una reserva de coordinación, no telemetría de presencia.
- Un repositorio sin lock no tiene exclusión mutua garantizada: se necesitan SHA/versiones, cambios seguros o coordinación del propietario.
- Un repositorio público derivado jamás autoriza publicar fuentes restringidas; la seguridad y revisión humana del origen prevalecen.
- La cola no sustituye la autoridad del repositorio de origen, sus deadlines, aprobaciones ni responsabilidades.
- Si un servicio externo no está disponible o el usuario debe aprobar una acción, no afirmar sincronización.

## Pruebas recomendadas

Simular (a) repositorio A ocupado, B disponible → elegir B; (b) varios candidatos en A → comprobar una sola vez A; (c) A vuelve a libre → re-elegible; (d) todos ocupados → salida limpia; después hacer prueba real de dos trabajadores con claims/versiones y productos comprobados. Compartir diagramas y ejemplos anonimizados, sin tokens ni datos del usuario.
