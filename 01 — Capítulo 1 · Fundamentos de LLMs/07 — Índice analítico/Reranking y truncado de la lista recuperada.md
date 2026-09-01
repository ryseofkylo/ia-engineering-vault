---
tags:
  - ficha
  - capitulo-1
seccion: "1.6"
---

# Reranking y truncado de la lista recuperada

> **En una línea.** Son las dos palancas para mitigar la degradación posicional: reordenar los documentos recuperados para empujar lo relevante hacia el principio, y recortar la lista cuando los últimos documentos no aportan.

> [!info] Ficha de consulta
> Esto es el índice analítico, no el libro. **El desarrollo completo está en [[1.6 — Por qué pasa y qué hacer al respecto|§1.6]]**

---

## La idea, en corto

**Reranking.** Reordenar los documentos que trajo el retriever antes de pegarlos en el prompt. El retriever ordena por similitud de embeddings, que es una señal barata y ruidosa. Un reranker —típicamente un cross-encoder, que mira la consulta y el documento juntos— reordena mejor pero es más caro. La consecuencia de *lost in the middle* es que **el reranking vale doble**: no sólo mejora qué está arriba, sino que empuja lo bueno a la posición donde el modelo efectivamente mira.

**Truncado de la lista** (*ranked list truncation*). Recuperar menos documentos cuando corresponde. Si el documento 15 tiene un score de similitud muy bajo, incluirlo no aporta información y sí agrega zona muerta, latencia y costo. Se puede truncar por cantidad fija, por umbral de score, o por caída relativa entre documentos consecutivos.

## Conectado con

[[Lost in the middle]] · [[Primacy y recency bias]] · [[Más contexto no es mejor]] · [[Closed-book y oracle como baselines]] · [[Costo por token]]

---

**Leer el desarrollo:** [[1.6 — Por qué pasa y qué hacer al respecto]] · **Índice del capítulo:** [[1.0 — Presentación del capítulo]]
