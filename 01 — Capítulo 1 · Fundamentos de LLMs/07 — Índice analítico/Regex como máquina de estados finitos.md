---
tags:
  - ficha
  - capitulo-1
seccion: "1.13"
---

# Regex como máquina de estados finitos

> **En una línea.** Toda expresión regular equivale a una máquina de estados finitos, y eso es lo que permite saber, en cada paso de generación, exactamente qué tokens están permitidos y cuáles hay que prohibir.

> [!info] Ficha de consulta
> Esto es el índice analítico, no el libro. **El desarrollo completo está en [[1.13 — Constrained decoding|§1.13]]**

---

## La idea, en corto

Es el truco conceptual detrás de `outlines`.

Una regex se puede compilar a un autómata: un grafo de estados donde cada transición consume un carácter. En cualquier estado, hay un conjunto **finito y conocido** de caracteres que pueden venir a continuación; todo lo demás lleva a un estado de error.

## Conectado con

[[Constrained decoding]] · [[Cómo se fuerza un formato]] · [[Logits y softmax]] · [[Pre-tokenización por regex]] · [[Salida estructurada]]

---

**Leer el desarrollo:** [[1.13 — Constrained decoding]] · **Índice del capítulo:** [[1.0 — Presentación del capítulo]]
