---
tags:
  - ficha
  - capitulo-1
seccion: "1.5"
---

# Lost in the middle

> **En una línea.** Es el hallazgo de que un modelo usa mucho mejor la información que está al principio o al final de su contexto que la que está en el medio: la curva de accuracy contra posición tiene forma de U.

> [!info] Ficha de consulta
> Esto es el índice analítico, no el libro. **El desarrollo completo está en [[1.5 — Lost in the Middle|§1.5]]**
> y también se lo trata en [[1.6 — Por qué pasa y qué hacer al respecto|§1.6]].

---

## La idea, en corto

Liu et al. (2023) hicieron un experimento limpio. Le dan al modelo *k* documentos de Wikipedia y una pregunta. **Exactamente uno** de los documentos contiene la respuesta; los otros *k*−1 son distractores relevantes pero incorrectos, traídos por un retriever real (Contriever afinado en MS-MARCO). Después mueven de lugar el documento correcto y miden la accuracy.

Si el modelo usara su contexto de forma pareja, la posición no debería importar. Importa muchísimo.

## Conectado con

[[Primacy y recency bias]] · [[Closed-book y oracle como baselines]] · [[Query-aware contextualization]] · [[Más contexto no es mejor]] · [[Reranking y truncado de la lista recuperada]] · [[Ventana de contexto]]

---

**Leer el desarrollo:** [[1.5 — Lost in the Middle]] · **Índice del capítulo:** [[1.0 — Presentación del capítulo]]
