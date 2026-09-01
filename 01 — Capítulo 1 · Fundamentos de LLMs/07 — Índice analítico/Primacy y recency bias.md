---
tags:
  - ficha
  - capitulo-1
seccion: "1.5"
---

# Primacy y recency bias

> **En una línea.** El modelo presta más atención al principio de su contexto (*primacy*) y al final (*recency*) que al medio; esos dos sesgos juntos son los que dibujan la curva en U.

> [!info] Ficha de consulta
> Esto es el índice analítico, no el libro. **El desarrollo completo está en [[1.5 — Lost in the Middle|§1.5]]**
> y también se lo trata en [[1.6 — Por qué pasa y qué hacer al respecto|§1.6]].

---

## La idea, en corto

El paper de Liu et al. midió cuál de los dos explica el fenómeno y encontró algo interesante: **ninguno solo lo explica**. Compararon MPT-30B (base, sin instruction tuning) contra MPT-30B-Instruct, y **los dos muestran la U**. El instruction tuning sube la accuracy absoluta y achica un poco la brecha entre el mejor y el peor caso (de casi 10 puntos a alrededor de 4), pero no crea ni elimina la forma.

En experimentos con Llama-2 de distintos tamaños encontraron además un matiz de escala: los modelos de 7B son **sólo** recency-biased, y la U completa recién aparece en 13B y 70B. La primacía parece emerger con el tamaño.

## Conectado con

[[Lost in the middle]] · [[Query-aware contextualization]] · [[Reranking y truncado de la lista recuperada]] · [[Ventana de contexto]]

---

**Leer el desarrollo:** [[1.5 — Lost in the Middle]] · **Índice del capítulo:** [[1.0 — Presentación del capítulo]]
