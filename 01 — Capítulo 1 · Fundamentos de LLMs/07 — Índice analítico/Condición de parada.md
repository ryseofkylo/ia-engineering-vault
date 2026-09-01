---
tags:
  - ficha
  - capitulo-1
seccion: "1.10"
---

# Condición de parada

> **En una línea.** Es la regla que decide cuándo el modelo deja de generar: o llegó a un token especial de fin, o alcanzó el máximo de tokens que le permitiste.

> [!info] Ficha de consulta
> Esto es el índice analítico, no el libro. **El desarrollo completo está en [[1.10 — Logprobs, parada y test time compute|§1.10]]**
> y también se lo trata en [[1.4 — La ventana de contexto|§1.4]].

---

## La idea, en corto

**1. Tokens de parada.** El modelo genera un token especial como `<|endoftext|>` y ahí se corta. Es la forma "natural": el modelo decidió que terminó. También podés definir *stop sequences* propias: strings que, si aparecen, cortan la generación.

**2. Cantidad máxima de tokens.** Un tope duro (`max_tokens`). Es rápido y predecible, pero **puede cortar la respuesta a la mitad**.

## Conectado con

[[Tokens especiales]] · [[Ventana de contexto]] · [[Costo por token]] · [[JSON mode]] · [[Salida estructurada]]

---

**Leer el desarrollo:** [[1.10 — Logprobs, parada y test time compute]] · **Índice del capítulo:** [[1.0 — Presentación del capítulo]]
