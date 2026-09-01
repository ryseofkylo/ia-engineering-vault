---
tags:
  - ficha
  - capitulo-1
seccion: "1.9"
---

# Top-p (nucleus sampling)

> **En una línea.** Top-p ordena los tokens por probabilidad, los va sumando hasta llegar al umbral *p*, y sortea sólo entre esos: un corte por **masa de probabilidad acumulada**, que se adapta solo a cada contexto.

> [!info] Ficha de consulta
> Esto es el índice analítico, no el libro. **El desarrollo completo está en [[1.9 — Top-k y top-p|§1.9]]**

---

## La idea, en corto

El procedimiento: ordenás las probabilidades de mayor a menor, las vas acumulando, y parás cuando la suma alcanza *p*. Ese conjunto —el "núcleo" o *nucleus*, de ahí el nombre— es entre lo que se sortea.

El ejemplo canónico. Probabilidades: `sí=60 %`, `tal vez=35 %`, `no=4 %`, `otro=1 %`.

## Conectado con

[[Logits y softmax]] · [[Top-k]] · [[Temperature]] · [[Greedy decoding y temperature 0]] · [[Test time compute]]

---

**Leer el desarrollo:** [[1.9 — Top-k y top-p]] · **Índice del capítulo:** [[1.0 — Presentación del capítulo]]
