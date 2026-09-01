---
tags:
  - ficha
  - capitulo-1
seccion: "1.15"
---

# Perplexity

> **En una línea.** Es una medida de la incertidumbre de un modelo de lenguaje al predecir la palabra siguiente: más baja es mejor, y se usa como termómetro barato del daño que causó una cuantización.

> [!info] Ficha de consulta
> Esto es el índice analítico, no el libro. **El desarrollo completo está en [[1.15 — Precisión numérica y la idea de cuantizar|§1.15]]**

---

## La idea, en corto

Intuitivamente: **entre cuántas opciones el modelo está efectivamente dudando** en cada paso. Una perplexity de 10 significa que, en promedio, es como si estuviera eligiendo al azar entre 10 alternativas igualmente probables.

Formalmente es la exponencial de la entropía cruzada promedio: se le da al modelo un texto que no vio, se mide qué probabilidad le asignaba a cada token real, y se agrega. Es matemáticamente la misma información que los [[Logprobs]], en otra escala.

## Conectado con

[[Cuantización]] · [[Logprobs]] · [[Modelo grande cuantizado vs modelo chico completo]] · [[Closed-book y oracle como baselines]] · [[PTQ y QAT]]

---

**Leer el desarrollo:** [[1.15 — Precisión numérica y la idea de cuantizar]] · **Índice del capítulo:** [[1.0 — Presentación del capítulo]]
