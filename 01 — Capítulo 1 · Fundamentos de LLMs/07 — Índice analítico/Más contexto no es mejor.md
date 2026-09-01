---
tags:
  - ficha
  - capitulo-1
seccion: "1.6"
---

# Más contexto no es mejor

> **En una línea.** Meterle más documentos al modelo tiene rendimientos decrecientes que llegan rápido: el rendimiento del lector se satura mucho antes que el recall del retriever, así que a partir de cierto punto sólo estás pagando latencia y tokens.

> [!info] Ficha de consulta
> Esto es el índice analítico, no el libro. **El desarrollo completo está en [[1.6 — Por qué pasa y qué hacer al respecto|§1.6]]**

---

## La idea, en corto

Es el hallazgo más directamente aplicable a tu trabajo.

Montaron un sistema retriever-reader estándar: Contriever recupera *k* documentos de Wikipedia para una consulta de NaturalQuestions-Open, y el modelo responde con esos documentos en el prompt. Después midieron dos cosas en función de *k*:

## Conectado con

[[Lost in the middle]] · [[Reranking y truncado de la lista recuperada]] · [[Closed-book y oracle como baselines]] · [[Ventana de contexto]] · [[Costo por token]]

---

**Leer el desarrollo:** [[1.6 — Por qué pasa y qué hacer al respecto]] · **Índice del capítulo:** [[1.0 — Presentación del capítulo]]
