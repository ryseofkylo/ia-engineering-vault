---
tags:
  - ficha
  - capitulo-1
seccion: "1.7"
---

# Logits y softmax

> **En una línea.** En cada paso de generación el modelo produce un *logit* —un número crudo, sin normalizar— por cada token del vocabulario, y softmax convierte ese vector de números en probabilidades que suman 1.

> [!info] Ficha de consulta
> Esto es el índice analítico, no el libro. **El desarrollo completo está en [[1.7 — Logits, softmax y azar|§1.7]]**
> y también se lo trata en [[1.13 — Constrained decoding|§1.13]].

---

## La idea, en corto

Esta es la pieza central de toda la generación, y una vez que la ves, tres lecturas del capítulo se acomodan solas.

En cada paso, el modelo mira todo lo que hay hasta ahora y produce un **vector de logits**: un número por cada token del vocabulario. Con `cl100k_base` eso son ~100.277 números, en cada paso. Un logit alto significa "este token me parece probable"; uno bajo, lo contrario. Pero no son probabilidades: pueden ser negativos y no suman nada en particular.

## Conectado con

[[Temperature]] · [[Top-k]] · [[Top-p (nucleus sampling)]] · [[Greedy decoding y temperature 0]] · [[Logprobs]] · [[Constrained decoding]] · [[Vocabulario y vocab size]]

---

**Leer el desarrollo:** [[1.7 — Logits, softmax y azar]] · **Índice del capítulo:** [[1.0 — Presentación del capítulo]]
