---
tags:
  - ficha
  - capitulo-1
seccion: "1.8"
---

# Temperature

> **En una línea.** Temperature es un número por el que se **dividen los logits antes del softmax**: valores bajos agrandan la ventaja del token más probable (salida consistente y aburrida), valores altos la achican (salida creativa y riesgosa).

> [!info] Ficha de consulta
> Esto es el índice analítico, no el libro. **El desarrollo completo está en [[1.8 — Temperature|§1.8]]**

---

## La idea, en corto

**Los logits se dividen por T antes de la exponencial.** Eso es todo.

Rango típico: **0 a 2**. Valor de equilibrio habitual: **0.7**.

## Conectado con

[[Logits y softmax]] · [[Greedy decoding y temperature 0]] · [[Top-k]] · [[Top-p (nucleus sampling)]] · [[No determinismo del LLM]] · [[Alucinación]]

---

**Leer el desarrollo:** [[1.8 — Temperature]] · **Índice del capítulo:** [[1.0 — Presentación del capítulo]]
