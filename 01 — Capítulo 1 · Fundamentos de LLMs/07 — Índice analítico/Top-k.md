---
tags:
  - ficha
  - capitulo-1
seccion: "1.9"
---

# Top-k

> **En una línea.** Top-k se queda con los *k* tokens de logit más alto, descarta todo el resto, y sortea sólo entre esos: un corte de cantidad **fija**.

> [!info] Ficha de consulta
> Esto es el índice analítico, no el libro. **El desarrollo completo está en [[1.9 — Top-k y top-p|§1.9]]**

---

## La idea, en corto

Después de calcular los logits, se ordenan de mayor a menor, se toman los *k* primeros, se aplica softmax **sólo sobre esos k** y se sortea. Los demás tokens quedan con probabilidad cero.

Valores típicos: **entre 50 y 500**, muchísimo menos que el tamaño del vocabulario.

## Conectado con

[[Logits y softmax]] · [[Top-p (nucleus sampling)]] · [[Temperature]] · [[Greedy decoding y temperature 0]] · [[Constrained decoding]]

---

**Leer el desarrollo:** [[1.9 — Top-k y top-p]] · **Índice del capítulo:** [[1.0 — Presentación del capítulo]]
