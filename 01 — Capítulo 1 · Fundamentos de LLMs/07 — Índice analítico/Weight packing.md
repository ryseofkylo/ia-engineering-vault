---
tags:
  - ficha
  - capitulo-1
seccion: "1.16"
---

# Weight packing

> **En una línea.** Como el hardware no maneja datos de 4 bits en memoria, se empaquetan **dos valores int4 en un solo byte** — y la ganancia principal de int4 no es de cómputo sino de ancho de banda de memoria.

> [!info] Ficha de consulta
> Esto es el índice analítico, no el libro. **El desarrollo completo está en [[1.16 — El mecanismo de la cuantización|§1.16]]**

---

## La idea, en corto

Int4 tiene 16 valores posibles (`−8` a `7` con signo). Pero la memoria se direcciona en bytes, y casi ningún hardware sabe manejar nativamente un tipo de 4 bits.

La solución es empaquetar dos valores en un byte: uno en los 4 bits bajos, otro en los 4 altos.

## Conectado con

[[Cuantización]] · [[Precisión numérica]] · [[Cuantización afín]] · [[Granularidad de la cuantización]] · [[VRAM]] · [[FP8]]

---

**Leer el desarrollo:** [[1.16 — El mecanismo de la cuantización]] · **Índice del capítulo:** [[1.0 — Presentación del capítulo]]
