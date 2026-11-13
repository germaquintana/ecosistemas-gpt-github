# Comenzar aquí — entiende lo que adoptarías en cinco minutos

Esta biblioteca **no es un software que se instala**. Es una metodología de trabajo con plantillas y decisiones configurables. Puedes adoptar una parte y descartar el resto.

## 1. Mapa del ecosistema

```mermaid
flowchart TB
  H["Decisiones de la persona"] --> O["Objetivos y resultados esperados"]
  O --> T["Proyectos y entregables"]
  T --> AI["Asistente de IA con instrucciones"]
  AI --> GH["GitHub: estado, tareas, versiones y RUN"]
  AI --> FS["Fuentes y documentos originales"]
  FS -. "Acceso autorizado" .-> AI
  GH --> QA["Validación y evidencia"]
  QA --> H
  AI -. "Solo si es útil y autorizado" .-> PL["Drive · Gmail · Trello · Calendar · otras apps"]
```

## 2. Los siete compromisos de buenas prácticas

| Nº | Si adoptas esta práctica... | Te comprometes a... |
|---|---|---|
| 1 | **Definir antes de ejecutar** | Expresar objetivo, resultado, responsable, plazo real y criterio de término |
| 2 | **Conservar fuentes confiables** | No sustituir originales con resúmenes; citar dónde está cada evidencia |
| 3 | **Versionar decisiones** | Mantener instrucciones, estado, cambios y próxima acción en GitHub |
| 4 | **Evitar duplicaciones** | Una tarea por resultado; consultar antes de crear otra |
| 5 | **Respetar privacidad** | No entregar datos, permisos o credenciales que no te pertenezcan |
| 6 | **Delimitar autonomía** | Reservar para revisión humana las acciones sensibles o irreversibles |
| 7 | **Comprobar entregas** | No declarar éxito sin resultado, prueba y evidencia verificables |

Son **compromisos voluntarios de trabajo**, no una relación contractual con el autor del repositorio.

## 3. Qué se configura y qué no

- **Base recomendada:** un proyecto propio (preferentemente privado), README, objetivo, `AGENTS.md` ajustado, tareas/issues y estado breve.
- **Según necesidad:** Google Drive u otro espacio documental, plantillas, métricas, CI, pruebas, bitácoras.
- **Solo con autorización:** conectores a correo, calendarios, datos institucionales, automatizaciones, escrituras externas y publicación.
- **Nunca de forma automática por abrir el enlace:** ninguna aplicación obtiene acceso; no se crean tareas, correos ni calendarios; no se instalan extensiones.

## Novedad 13/11/2026: interacción sencilla y continuidad

Si usas una bandeja humana opcional (Trello, Issues u otra), evita exigir tanto un comentario como una marca de checklist: **cualquiera de las dos acciones puede bastar**, según su significado. No impongas códigos especiales como `IA:` si la integración puede interpretar lenguaje normal. Una casilla marcada acredita solo el hecho descrito; no sustituye autorizaciones de actos formales.

Una tarea que depende de una persona **espera en su expediente**; las demás tareas que sí son seguras y ejecutables pueden avanzar. El bloqueo técnico del repositorio protege escrituras breves, no debe sostenerse por una respuesta humana pendiente. Los bloqueos ajenos no se liberan sin investigación y control.

[Lee la actualización del 13/11/2026 y adapta tu sistema existente](ACTUALIZACION_2026-11-13.md). Su aplicación requiere permisos y pruebas reales.

## 4. Tu primera práctica

Elige un proyecto pequeño, como organizar materiales de una actividad. Define un entregable que puedas revisar, crea un repositorio privado, conserva allí las instrucciones y el estado, y realiza una sola tarea. Después comprueba y documenta el resultado.

## 5. Pide una explicación adaptada a ti

Abre [PROMPT_PARA_CHATGPT.md](PROMPT_PARA_CHATGPT.md). Copia el texto y pégalo en ChatGPT junto a la URL de esta biblioteca. Recibirás un mapa, tabla de prácticas y configuración de inicio. **La IA deberá leer el repositorio en vivo** y declarar cualquier archivo inaccesible, en vez de inventar contenidos.

Puedes consultar [un ejemplo de cómo debería verse la respuesta](EJEMPLO_RESPUESTA_ESQUEMATICA.md).
