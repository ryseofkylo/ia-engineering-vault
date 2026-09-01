---
tags:
  - ficha
  - capitulo-1
seccion: "1.12"
---

# Reintentos con validación

> **En una línea.** Es el patrón de validar la respuesta y, si falla, volver a pedirla incluyendo el mensaje de error para que el modelo se corrija; es una red de seguridad efectiva y con un costo que hay que contar.

> [!info] Ficha de consulta
> Esto es el índice analítico, no el libro. **El desarrollo completo está en [[1.12 — Las cuatro estrategias|§1.12]]**

---

## La idea, en corto

1. Pedís la respuesta con un esquema pydantic.
2. Validás.
3. Si `ValidationError`, volvés a llamar **agregando el error al contexto**: "devolviste esto, falló por esto, corregilo".
4. Repetís hasta un máximo de intentos.

El paso 3 es lo que lo hace funcionar. No es reintentar igual y esperar suerte: es darle al modelo la información de qué estuvo mal.

## Conectado con

[[Pydantic como contrato de datos]] · [[Cómo se fuerza un formato]] · [[Constrained decoding]] · [[Condición de parada]] · [[Costo por token]]

---

**Leer el desarrollo:** [[1.12 — Las cuatro estrategias]] · **Índice del capítulo:** [[1.0 — Presentación del capítulo]]
