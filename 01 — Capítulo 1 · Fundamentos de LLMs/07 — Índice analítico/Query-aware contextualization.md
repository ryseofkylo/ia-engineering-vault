---
tags:
  - ficha
  - capitulo-1
seccion: "1.6"
---

# Query-aware contextualization

> **En una línea.** Es poner la pregunta **antes y después** de los datos en vez de sólo después, para que un modelo decoder-only pueda tenerla en cuenta mientras procesa cada documento.

> [!info] Ficha de consulta
> Esto es el índice analítico, no el libro. **El desarrollo completo está en [[1.6 — Por qué pasa y qué hacer al respecto|§1.6]]**

---

## La idea, en corto

Un modelo decoder-only sólo puede atender a los tokens **anteriores**. Si tu prompt es `[documentos] [pregunta]`, entonces cuando el modelo está procesando el documento 3 todavía no vio la pregunta: lo contextualiza a ciegas.

Los modelos encoder-decoder no tienen ese problema, porque su encoder es bidireccional y procesa cada documento sabiendo qué viene después. El paper observó que esos modelos aguantan mejor los cambios de posición (Flan-UL2 tiene apenas 1,9 puntos de diferencia entre el mejor y el peor caso... **pero sólo dentro del largo con el que fue entrenado**; más allá de sus 2048 tokens de entrenamiento, la U reaparece).

## Conectado con

[[Lost in the middle]] · [[Primacy y recency bias]] · [[Reranking y truncado de la lista recuperada]] · [[Ventana de contexto]]

---

**Leer el desarrollo:** [[1.6 — Por qué pasa y qué hacer al respecto]] · **Índice del capítulo:** [[1.0 — Presentación del capítulo]]
