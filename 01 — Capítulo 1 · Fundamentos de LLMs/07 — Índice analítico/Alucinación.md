---
tags:
  - ficha
  - capitulo-1
seccion: "1.7"
---

# Alucinación

> **En una línea.** Es cuando el modelo produce contenido plausible pero falso, y no es un defecto separable: es la misma propiedad probabilística que le permite ser creativo, vista desde el otro lado.

> [!info] Ficha de consulta
> Esto es el índice analítico, no el libro. **El desarrollo completo está en [[1.7 — Logits, softmax y azar|§1.7]]**
> y también se lo trata en [[1.13 — Constrained decoding|§1.13]].

---

## La idea, en corto

El punto conceptual es incómodo y hay que entenderlo bien: **la creatividad y la alucinación son el mismo mecanismo.**

El modelo no consulta una base de datos de hechos. Genera el token siguiente más probable según los patrones que aprendió. Cuando esos patrones coinciden con la realidad, lo llamamos "respuesta correcta". Cuando no, lo llamamos alucinación. **El proceso interno es idéntico en los dos casos.** Por eso no se puede "apagar" la alucinación sin apagar también la capacidad generativa.

## Conectado con

[[No determinismo del LLM]] · [[Temperature]] · [[Logprobs]] · [[Test time compute]] · [[Lost in the middle]] · [[Pydantic como contrato de datos]]

---

**Leer el desarrollo:** [[1.7 — Logits, softmax y azar]] · **Índice del capítulo:** [[1.0 — Presentación del capítulo]]
