---
tags:
  - ficha
  - capitulo-1
seccion: "1.4"
---

# Ventana de contexto

> **En una línea.** Es la cantidad máxima de tokens —entrada más salida— que el modelo puede tener en cuenta en una sola llamada; es un límite duro, contado en tokens y no en palabras.

> [!info] Ficha de consulta
> Esto es el índice analítico, no el libro. **El desarrollo completo está en [[1.4 — La ventana de contexto|§1.4]]**
> y también se lo trata en [[1.18 — VRAM, KV cache y offload|§1.18]].

---

## La idea, en corto

El modelo es una función sin memoria: recibe una secuencia de tokens y devuelve el siguiente. La ventana de contexto es el largo máximo de esa secuencia.

1. **La ventana incluye la salida.** Si el modelo tiene 8K de ventana y tu prompt ocupa 7.500 tokens, te quedan 500 para la respuesta. Muchos proveedores tienen además un límite separado de tokens de salida.
2. **Es un límite técnico, no una sugerencia.** Pasarte no degrada: falla, o trunca silenciosamente. El truncado silencioso es el peor de los dos, porque no te enterás.
3. **Se cuenta en tokens**, y todo cuenta: el system prompt, los ejemplos few-shot, el historial, los delimitadores de rol, la pregunta.

## Conectado con

[[Token]] · [[Costo por token]] · [[Tokens especiales]] · [[Lost in the middle]] · [[Más contexto no es mejor]] · [[KV cache]] · [[VRAM]]

---

**Leer el desarrollo:** [[1.4 — La ventana de contexto]] · **Índice del capítulo:** [[1.0 — Presentación del capítulo]]
