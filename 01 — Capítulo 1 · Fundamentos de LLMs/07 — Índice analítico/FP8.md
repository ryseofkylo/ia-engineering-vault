---
tags:
  - ficha
  - capitulo-1
seccion: "1.16"
---

# FP8

> **En una línea.** Es un tipo de 8 bits que conserva la estructura de punto flotante (signo, exponente, mantisa) en vez de ser un entero, y retiene más precisión que int8 en algunos escenarios — pero necesita hardware específico.

> [!info] Ficha de consulta
> Esto es el índice analítico, no el libro. **El desarrollo completo está en [[1.16 — El mecanismo de la cuantización|§1.16]]**

---

## La idea, en corto

Int8 es un entero: 256 valores repartidos de forma **uniforme** en el rango. FP8 es punto flotante: 256 valores repartidos de forma **no uniforme**, con más resolución cerca del cero y menos en los extremos. Para distribuciones de pesos, que se concentran cerca del cero, eso puede ser mejor.

Se usa en el esquema **A8W8**, que cuantiza tanto **activaciones (A)** como **pesos (W)** a 8 bits. Eso es distinto de la mayoría de los esquemas que vas a ver, donde sólo se cuantizan los pesos.

## Conectado con

[[Precisión numérica]] · [[Cuantización]] · [[Weight packing]] · [[Cuantización afín]] · [[Compute capability]]

---

**Leer el desarrollo:** [[1.16 — El mecanismo de la cuantización]] · **Índice del capítulo:** [[1.0 — Presentación del capítulo]]
