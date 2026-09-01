---
tags:
  - ficha
  - capitulo-1
seccion: "1.16"
---

# Granularidad de la cuantización

> **En una línea.** Es cuántos pesos comparten el mismo par de parámetros `scale` y `zero-point`: uno solo para todo el tensor (simple, impreciso) o uno por canal o por grupo de N pesos (más preciso, un poco más caro).

> [!info] Ficha de consulta
> Esto es el índice analítico, no el libro. **El desarrollo completo está en [[1.16 — El mecanismo de la cuantización|§1.16]]**
> y también se lo trata en [[1.17 — Elegir un modelo|§1.17]].

---

## La idea, en corto

Los parámetros `S` y `Z` de [[Cuantización afín]] se calculan sobre un conjunto de pesos. La pregunta es: ¿qué tan grande es ese conjunto?

El porqué es directo: si un tensor tiene un peso atípico enorme, `val_max` se dispara, la escala se agranda, y **todos** los pesos normales pierden resolución. Con grupos chicos, el outlier arruina sólo su grupo.

## Conectado con

[[Cuantización afín]] · [[Cuantización]] · [[Precisión numérica]] · [[PTQ y QAT]] · [[Weight packing]] · [[Ollama]]

---

**Leer el desarrollo:** [[1.16 — El mecanismo de la cuantización]] · **Índice del capítulo:** [[1.0 — Presentación del capítulo]]
