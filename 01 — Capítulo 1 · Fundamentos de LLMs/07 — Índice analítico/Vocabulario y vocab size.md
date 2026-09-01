---
tags:
  - ficha
  - capitulo-1
seccion: "1.2"
---

# Vocabulario y vocab size

> **En una línea.** El vocabulario es la lista completa de tokens que el modelo conoce, y su tamaño es una decisión de diseño con costos en las dos direcciones: chico da secuencias largas, grande da una capa de salida enorme.

> [!info] Ficha de consulta
> Esto es el índice analítico, no el libro. **El desarrollo completo está en [[1.2 — Byte Pair Encoding|§1.2]]**
> y también se lo trata en [[1.7 — Logits, softmax y azar|§1.7]].

---

## La idea, en corto

El vocabulario es un diccionario: `token → ID entero`. Su tamaño (*vocab size*) se decide **antes** de entrenar el tokenizer, porque es la cantidad de vueltas del bucle de BPE: vocab size = 256 bytes iniciales + cantidad de merges + tokens especiales.

Duplicar el vocabulario mejora la cobertura de idiomas y dominios que no son inglés, y acorta las secuencias.

## Conectado con

[[Token]] · [[Byte Pair Encoding (BPE)]] · [[Tokens especiales]] · [[Logits y softmax]] · [[Costo por token]]

---

**Leer el desarrollo:** [[1.2 — Byte Pair Encoding]] · **Índice del capítulo:** [[1.0 — Presentación del capítulo]]
