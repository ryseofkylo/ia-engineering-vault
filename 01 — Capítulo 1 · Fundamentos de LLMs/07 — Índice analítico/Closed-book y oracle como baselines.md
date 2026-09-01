---
tags:
  - ficha
  - capitulo-1
seccion: "1.5"
---

# Closed-book y oracle como baselines

> **En una línea.** *Closed-book* es el modelo contestando sin ningún documento (el piso) y *oracle* es el modelo con únicamente el documento correcto (el techo): sin esas dos referencias, cualquier número de accuracy de tu sistema RAG es ininterpretable.

> [!info] Ficha de consulta
> Esto es el índice analítico, no el libro. **El desarrollo completo está en [[1.5 — Lost in the Middle|§1.5]]**
> y también se lo trata en [[1.6 — Por qué pasa y qué hacer al respecto|§1.6]].

---

## La idea, en corto

Un baseline es un número contra el cual comparar. El paper de Liu et al. define dos, y son de los conceptos más portables de todo el capítulo:

Estos dos números son los que le dan sentido al hallazgo central: la curva en U cae **por debajo del closed-book** en el peor caso. Sin la fila de closed-book, "cayó 20 puntos" es un número triste. Con ella, es un resultado alarmante.

## Conectado con

[[Lost in the middle]] · [[Más contexto no es mejor]] · [[Reranking y truncado de la lista recuperada]]

---

**Leer el desarrollo:** [[1.5 — Lost in the Middle]] · **Índice del capítulo:** [[1.0 — Presentación del capítulo]]
