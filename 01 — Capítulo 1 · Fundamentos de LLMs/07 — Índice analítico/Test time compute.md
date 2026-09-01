---
tags:
  - ficha
  - capitulo-1
seccion: "1.10"
---

# Test time compute

> **En una línea.** Es generar varias salidas para el mismo pedido y quedarse con la mejor, gastando más cómputo en el momento de la inferencia en vez de en el entrenamiento.

> [!info] Ficha de consulta
> Esto es el índice analítico, no el libro. **El desarrollo completo está en [[1.10 — Logprobs, parada y test time compute|§1.10]]**

---

## La idea, en corto

La idea: *una forma simple de mejorar el rendimiento de un modelo es generar múltiples salidas y elegir la mejor*.

**1. Por logprob promedio.** Te quedás con la salida a la que el propio modelo le asignó más probabilidad, normalizada por largo. Es lo que hace el parámetro `best_of` de OpenAI: con `best_of=10` genera 10 y devuelve la de mayor logprob promedio.

## Conectado con

[[Logprobs]] · [[Top-p (nucleus sampling)]] · [[Temperature]] · [[No determinismo del LLM]] · [[Alucinación]] · [[Costo por token]]

---

**Leer el desarrollo:** [[1.10 — Logprobs, parada y test time compute]] · **Índice del capítulo:** [[1.0 — Presentación del capítulo]]
