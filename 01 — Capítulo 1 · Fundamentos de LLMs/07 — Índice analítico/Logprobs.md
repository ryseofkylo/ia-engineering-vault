---
tags:
  - ficha
  - capitulo-1
seccion: "1.10"
---

# Logprobs

> **En una línea.** Son las probabilidades en escala logarítmica; se usan porque con vocabularios de ~100.000 tokens las probabilidades son tan chicas que se pierden por *underflow*, y porque en escala log las multiplicaciones se vuelven sumas.

> [!info] Ficha de consulta
> Esto es el índice analítico, no el libro. **El desarrollo completo está en [[1.10 — Logprobs, parada y test time compute|§1.10]]**

---

## La idea, en corto

**1. Underflow.** La probabilidad de una secuencia es el producto de las probabilidades de cada token. Con secuencias largas eso da números como 0,0000000000001, y el punto flotante deja de representarlos con precisión. En escala logarítmica son números manejables como −13.

**2. Sumar en vez de multiplicar.** Un logaritmo convierte productos en sumas, que son más rápidas y numéricamente más estables.

## Conectado con

[[Logits y softmax]] · [[Test time compute]] · [[Alucinación]] · [[No determinismo del LLM]] · [[Vocabulario y vocab size]]

---

**Leer el desarrollo:** [[1.10 — Logprobs, parada y test time compute]] · **Índice del capítulo:** [[1.0 — Presentación del capítulo]]
