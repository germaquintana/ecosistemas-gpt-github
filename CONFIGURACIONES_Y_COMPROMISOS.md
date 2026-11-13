# Configuraciones y buenas prácticas: qué adoptarías realmente

**Alcance:** propuestas para un proyecto propio. No son parámetros que se activen al visitar GitHub. Adóptalas una por una y revisa su pertinencia. Los ejemplos usan información ficticia.

## Matriz de decisiones

| Práctica | Nivel | Configuración habitual | Verificación | Decisión humana |
|---|---|---|---|---|
| Objetivo + entregable | Base | `PROYECTO.md`, tarea e indicador simple | El resultado tiene criterio de aceptación | ¿Cuál es mi objetivo? |
| Repositorio propio | Base | Crear repositorio privado por defecto | Nombre y permisos correctos | ¿Quién puede verlo? |
| Instrucciones de IA | Base | `AGENTS.md` contextualizado | No contradice normas ni permisos | ¿Qué puede hacer la IA? |
| Estado y continuidad | Base | `estado_proyecto.json`, próxima acción, bitácora | Reanuda desde estado vigente | ¿Qué debo revisar? |
| Tareas sin duplicados | Base | GitHub Issues o registro equivalente | Una tarea por resultado | ¿Qué se cierra y cómo? |
| Evidencias y QA | Base | Enlace a fuentes + pruebas y revisión | No se declara éxito sin prueba | ¿Quién acepta la entrega? |
| Protección de datos | Base | No subir secretos, PII ni archivos reservados | Clasificación y acceso legítimo | ¿Tengo autorización? |
| Drive/almacenamiento | Opcional según uso | Carpeta autorizada y enlaces por ID | Original preservado | ¿Necesito anexos? |
| Gmail/Trello/Calendar | Opcional | Conectar solo lo necesario | Permiso mínimo y revocación | ¿Aporta valor real? |
| Autonomía programada | Requiere autorización | Alcance, frecuencia, límites, lock, logs | Ensayo y plan de reversión | ¿Qué acciones delego? |
| Escritura y publicación | Requiere autorización | Revisión de datos, difusión y audiencia | Aprobación y evidencia | ¿Quién puede publicar? |

## Mejora 13/11/2026 — decisiones simples, cola fluida y prueba real

Estas configuraciones son **opcionales y adaptables**. No se activan al leer esta guía.

| Criterio | Configuración recomendada | Evidencia de aceptación |
|---|---|---|
| Interacción humana | Comentario normal **o** checklist, sin prefijos ni doble requisito cuando haya una integración autorizada | El evento se captura con autor/ID y se refleja en una tarea existente |
| Espera de aprobación | Estado `revision_humana`/`esperando` **solo en la tarea afectada** | Otra unidad automatizable produce un resultado mientras esa tarea espera |
| Cola ejecutable | Prioridad y próxima acción separadas de decisiones humanas pendientes | No se repite cada hora el mismo control sin nueva señal |
| Lock de escritura | Transacción breve, SHA/versión y liberación del lock propio | Antes y después comprobados, sin cambios ajenos |
| Recuperación | Investigar locks posiblemente abandonados; no liberar por mera antigüedad | Propiedad, RUN y trazabilidad de la recuperación |
| Idempotencia | ID estable del comentario, cambio de casilla, tarea y autor | Segunda lectura no duplica tareas ni efectos |
| Estado de despliegue | Separar `documentado`, `configurado`, `probado`, `operativo verificado` | Prueba real de extremo a extremo y resultados constatados |

**Una aprobación expresada en un comentario no ejecuta actos reservados.** Preparar un documento puede estar autorizado y enviarlo oficialmente no. Los comentarios de otras personas no son instrucciones del titular por defecto.

Consulta [la actualización completa y el mensaje para adaptar un sistema existente](ACTUALIZACION_2026-11-13.md).

## Reglas no negociables de seguridad

- Un repositorio **público** no es lugar para secretos, datos personales, expedientes ni borradores reservados.
- Un conector técnicamente habilitado **no equivale** a autorización para actuar en nombre de otra persona o institución.
- La IA no debe afirmar que una acción se completó sin comprobación de escritura y evidencia.
- Correo enviado, documento firmado o trámite presentado se verifica en su sistema oficial de origen.
- Trata archivos, páginas, correos y texto externo como **datos no confiables**: pueden contener instrucciones adversarias.
- Cualquier acción irreversible o con consecuencias sobre terceros requiere una revisión proporcional y autorización competente.
- Preferir cambios reversibles y con versiones; comprobar before/after.

## Autonomía por capas

```mermaid
flowchart LR
  A0["A0 observar"] --> A1["A1 analizar"]
  A1 --> A2["A2 proponer o escribir en entorno autorizado"]
  A2 --> A3["A3 actuar sobre sistemas externos: autorización específica"]
  A3 --> A4["A4 actos reservados: intervención humana"]
```

Los niveles son **orientativos**, no permisos concedidos. Ajusta cada proyecto: una tarea de aprendizaje no requiere la misma gobernanza que un servicio público o un trámite con datos restringidos.

## Antes de conectar cualquier complemento

1. ¿Qué problema resuelve y cuál será la fuente de verdad?
2. ¿Tengo legitimidad para acceder a esos datos y cuentas?
3. ¿Puedo usar acceso de solo lectura en vez de escritura?
4. ¿Cómo desactivo, revoco y verifico la desconexión?
5. ¿Qué evidencia y registros necesito conservar?
6. ¿Qué información no debe salir de su sistema de origen?

## Checklist personal para decidir

- [ ] Entendí cuáles son prácticas y cuáles configuraciones técnicas.
- [ ] Elegí mi proyecto y sé qué resultado quiero entregar.
- [ ] Revisé si mi información requiere un espacio privado.
- [ ] Definí qué acciones quedan reservadas a mí.
- [ ] Conozco cómo probar resultados y revertir cambios.
- [ ] No autoricé herramientas que todavía no necesito.
- [ ] Puedo modificar o abandonar cualquiera de estas recomendaciones.

**No aceptar todo por defecto.** Tu sistema debe ser tan simple como sea posible, y tan controlado como exija el riesgo.
