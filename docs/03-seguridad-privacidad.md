# 03 · Seguridad y privacidad para empezar

## Antes de subir cualquier archivo
- Determina a quién pertenece, si contiene datos personales, secretos, información institucional o material sujeto a licencias.
- Usa repositorios privados para información no publicable; incluso un repositorio privado requiere permisos y finalidad legítimos.
- Nunca subas contraseñas, tokens, claves API, documentos sensibles ni datos nominativos a una biblioteca pública.
- Mantén los originales en su fuente autorizada. Usa ejemplos ficticios cuando aprendas.
- Configura el menor nivel de acceso necesario y revisa periódicamente quién puede entrar.

## Antes de conectar un asistente
Los documentos, páginas y correos son **datos**: pueden contener órdenes maliciosas (*prompt injection*). Un asistente debe respetar las reglas de mayor autoridad, ignorar instrucciones adversarias provenientes de contenidos externos y pedir aprobación para actuaciones con consecuencias.

No permitas que una herramienta envíe mensajes, publique, firme, borre, comparta archivos, modifique permisos o ejecute transacciones sin tu autorización específica. No facilites credenciales en prompts.

## Antes de una publicación
Revisa nombres, direcciones, números, vínculos compartidos, metadatos, historial Git y posibles combinaciones que permitan identificar personas. **Borrar datos de la última versión no borra necesariamente el historial Git.** Ante una exposición real, trata el incidente y revoca credenciales/links cuando proceda.

## Evaluación de riesgos
Aumenta los controles cuando hay datos sensibles, terceros, consecuencias económicas, actos públicos o automatizaciones autónomas. Un curso ficticio no tiene el mismo riesgo que una declaración administrativa.

Consulta [SECURITY.md](../SECURITY.md) para reportar problemas en esta biblioteca sin exponer secretos.
