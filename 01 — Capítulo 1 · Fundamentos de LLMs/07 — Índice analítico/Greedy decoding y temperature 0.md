---
tags:
  - ficha
  - capitulo-1
seccion: "1.8"
---

# Greedy decoding y temperature 0

> **En una línea.** *Greedy decoding* es elegir siempre el token más probable, sin sortear; `temperature=0` es técnicamente eso mismo — un `argmax` sobre los logits.

> [!info] Ficha de consulta
> Esto es el índice analítico, no el libro. **El desarrollo completo está en [[1.8 — Temperature|§1.8]]**

---

## La idea, en corto

Es la estrategia más simple: en cada paso, quedate con el token de logit más alto. Sin aleatoriedad.

Formalmente, `temperature=0` es una división por cero, así que las implementaciones lo tratan como un caso especial y hacen directamente `argmax`. Dicho de otro modo: una temperatura de 0 técnicamente hace un argmax.

## Conectado con

[[Temperature]] · [[Logits y softmax]] · [[No determinismo del LLM]] · [[Top-k]] · [[Test time compute]]

---

**Leer el desarrollo:** [[1.8 — Temperature]] · **Índice del capítulo:** [[1.0 — Presentación del capítulo]]
