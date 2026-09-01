---
tags:
  - ficha
  - capitulo-1
seccion: "1.16"
---

# Cuantización afín

> **En una línea.** Es el método más común de cuantizar: mapear el rango real de valores float de un tensor al rango de enteros disponible, usando dos parámetros — `scale` (cuánto vale un escalón) y `zero-point` (qué entero representa el cero).

> [!info] Ficha de consulta
> Esto es el índice analítico, no el libro. **El desarrollo completo está en [[1.16 — El mecanismo de la cuantización|§1.16]]**

---

## La idea, en corto

Tenés un tensor de pesos en float32. Buscás su mínimo y su máximo, y mapeás ese rango `[val_min, val_max]` al rango de int8, típicamente `[−128, 127]`.

**Cuantizar y descuantizar:**

## Conectado con

[[Cuantización]] · [[Granularidad de la cuantización]] · [[Precisión numérica]] · [[PTQ y QAT]] · [[Weight packing]]

---

**Leer el desarrollo:** [[1.16 — El mecanismo de la cuantización]] · **Índice del capítulo:** [[1.0 — Presentación del capítulo]]
