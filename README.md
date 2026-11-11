# Ecosistemas GPT + GitHub · Guía abierta para colegas

**Aprende a organizar proyectos con un asistente de IA, GitHub y herramientas complementarias, de forma segura, verificable y adaptable.**

> Guía educativa de adopción voluntaria, versión 1.0 (11-11-2026). **Leer esta página no instala nada, no conecta cuentas ni concede permisos.** No es una política oficial de una institución, de OpenAI ni de GitHub.

## Implementar tu propio ecosistema directamente desde ChatGPT

**¿Quieres que ChatGPT te ayude a construir el sistema en TU cuenta de GitHub, en vez de solo explicarlo?** Usa la [guía de implementación paso a paso](IMPLEMENTAR_CON_CHATGPT.md). Contiene un mensaje único para copiar al chat, un diagnóstico mínimo, los archivos del proyecto, pruebas de verificación y un modelo seguro para conectar complementos opcionales.

> Abrir GitHub no instala ni ejecuta nada. El colega debe **pegar un mensaje de instrucción en su ChatGPT** y autorizar el acceso y las escrituras en su propio entorno. No se utilizan las cuentas del autor de esta guía.

**Enlace directo para enviar a un colega:** [IMPLEMENTAR_CON_CHATGPT.md](IMPLEMENTAR_CON_CHATGPT.md)

## ¿Te compartieron este repositorio? Comienza aquí

**[1. Entiende el sistema en 5 minutos](COMENZAR_AQUI.md)** · **[2. Consulta las prácticas y configuraciones](CONFIGURACIONES_Y_COMPROMISOS.md)** · **[3. Pide a ChatGPT un resumen esquemático y personalizado](PROMPT_PARA_CHATGPT.md)**

### ¿Quieres compartir esto con otra persona?

Envía el enlace [**Mensaje para compartir**](MENSAJE_PARA_COMPARTIR.md), o directamente el URL de este repositorio. Para obtener una **respuesta esquemática en ChatGPT** —arquitectura, prácticas, configuraciones recomendadas, componentes opcionales, riesgos y pasos de adopción— tu colega debe abrir [**PROMPT_PARA_CHATGPT.md**](PROMPT_PARA_CHATGPT.md), copiar el texto y pegarlo en su propia conversación de ChatGPT. El enlace por sí solo no ejecuta un asistente ni instala prácticas.

### Arquitectura en una mirada

```mermaid
flowchart TD
    P["👤 Persona responsable: define objetivos y autoriza"] --> IA["🤖 Asistente de IA: analiza, propone y ayuda a ejecutar"]
    IA --> G["📁 GitHub: versiones, reglas, tareas y bitácora"]
    IA --> D["📄 Fuentes autorizadas: Drive u otro almacén"]
    G <-->|"IDs, enlaces, referencias; no copiar todo"| D
    IA --> V["✅ Pruebas y revisión humana"]
    V --> P
    IA -. "Solo si se autoriza" .-> X["✉️ Gmail · 📅 Calendar · Trello · otros"]
```

### Qué prácticas propone adoptar

| Tema | Regla recomendada | Por qué |
|---|---|---|
| Dirección | Un objetivo claro y un entregable verificable | Evita tareas sin propósito |
| Fuente de verdad | Una autoridad por tipo de dato | Evita contradicciones |
| Continuidad | Estado, próxima acción y RUN versionados | Permite retomar sin empezar de cero |
| Seguridad | Mínimos permisos y fuentes autorizadas | Reduce riesgos |
| Autonomía | La IA actúa dentro de límites, con validaciones | Impide ejecuciones no deseadas |
| Calidad | Comprobar antes de declarar completado | Mejora fiabilidad |
| Modularidad | Complementos opcionales; conectar y desconectar | Reduce complejidad |

**No estás suscribiendo un servicio ni aceptando automáticamente ninguna configuración.** Adoptar una práctica exige decidirla y configurarla deliberadamente en *tu propio* proyecto.

## Ruta de aprendizaje

- [Guía rápida y explicaciones](COMENZAR_AQUI.md)
- [Prácticas, controles y niveles de adopción](CONFIGURACIONES_Y_COMPROMISOS.md)
- [Prompt listo para copiar en ChatGPT](PROMPT_PARA_CHATGPT.md)
- [Ejemplo esquemático de la respuesta que deberías recibir](EJEMPLO_RESPUESTA_ESQUEMATICA.md)
- [Tu primer proyecto](docs/01-primer-proyecto.md)
- [Arquitectura y autoridad de fuentes](docs/02-arquitectura.md)
- [Seguridad y privacidad](docs/03-seguridad-privacidad.md)
- [Gestión de objetivos y tareas](docs/04-gestion-proyectos.md)
- [Autonomía responsable](docs/05-autonomia-segura.md)
- [Integraciones modulares](docs/06-modularidad.md)
- [Plantilla para crear tu propio repositorio](plantilla-proyecto/README.md)

**Importante:** emplea repositorios privados para trabajo con información no destinada a publicación. Nunca copies credenciales, expedientes o datos personales a esta biblioteca pública. Usa ejemplos ficticios.

## Uso y mantenimiento

Este material se puede leer y compartir mediante enlaces. La licencia de reutilización aún requiere una decisión explícita del titular; mientras tanto, no presupongas una licencia abierta para redistribuir o adaptar los archivos. Consulta [licenciamiento](LICENCIAMIENTO.md) y [seguridad](SECURITY.md). Las mejoras se pueden proponer en las *Issues* públicas sin adjuntar información reservada.
