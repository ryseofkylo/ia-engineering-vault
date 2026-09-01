---
tags:
  - ficha
  - capitulo-1
seccion: "1.13"
---

# Constrained decoding

> **En una línea.** Es forzar el formato interviniendo en el sampling: en cada paso se enmascaran los logits de todos los tokens que romperían la gramática, así que generar algo inválido es literalmente imposible.

> [!info] Ficha de consulta
> Esto es el índice analítico, no el libro. **El desarrollo completo está en [[1.13 — Constrained decoding|§1.13]]**
> y también se lo trata en [[1.12 — Las cuatro estrategias|§1.12]].

---

## La idea, en corto

Es el nivel 4 de [[Cómo se fuerza un formato]], y el único que da una garantía en vez de una probabilidad alta.

1. El modelo calcula su vector de logits.
2. **Se filtran los logits**, dejando sólo los que cumplen la restricción.
3. Se samplea de ese conjunto reducido.

## Conectado con

[[Logits y softmax]] · [[Cómo se fuerza un formato]] · [[Regex como máquina de estados finitos]] · [[Pydantic como contrato de datos]] · [[Modelos locales vs API]] · [[Top-k]]

---

**Leer el desarrollo:** [[1.13 — Constrained decoding]] · **Índice del capítulo:** [[1.0 — Presentación del capítulo]]
