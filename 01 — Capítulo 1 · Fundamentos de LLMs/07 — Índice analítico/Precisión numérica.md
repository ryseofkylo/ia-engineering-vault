---
tags:
  - ficha
  - capitulo-1
seccion: "1.15"
---

# Precisión numérica

> **En una línea.** Es cuántos bits usás para guardar cada número del modelo; determina directamente cuánta memoria ocupa y cuánta precisión conservás.

> [!info] Ficha de consulta
> Esto es el índice analítico, no el libro. **El desarrollo completo está en [[1.15 — Precisión numérica y la idea de cuantizar|§1.15]]**
> y también se lo trata en [[1.16 — El mecanismo de la cuantización|§1.16]].

---

## La idea, en corto

Un peso es un número. Cuántos bits le dedicás es una decisión.

La distinción **exponente vs. mantisa** es la que explica todo: el exponente da el **rango** (qué tan grandes y chicos pueden ser los números) y la mantisa da la **precisión** (cuántos decimales distinguís).

## Conectado con

[[Cuantización]] · [[Cuantización afín]] · [[FP8]] · [[Weight packing]] · [[VRAM]] · [[KV cache]]

---

**Leer el desarrollo:** [[1.15 — Precisión numérica y la idea de cuantizar]] · **Índice del capítulo:** [[1.0 — Presentación del capítulo]]
