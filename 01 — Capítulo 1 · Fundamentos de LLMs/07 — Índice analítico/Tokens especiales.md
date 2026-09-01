---
tags:
  - ficha
  - capitulo-1
seccion: "1.2"
---

# Tokens especiales

> **En una línea.** Son tokens que no salen del algoritmo BPE sino que se agregan a mano al vocabulario para marcar estructura: dónde empieza un documento, dónde termina un turno de conversación, dónde va un hueco a completar.

> [!info] Ficha de consulta
> Esto es el índice analítico, no el libro. **El desarrollo completo está en [[1.2 — Byte Pair Encoding|§1.2]]**
> y también se lo trata en [[1.10 — Logprobs, parada y test time compute|§1.10]].

---

## La idea, en corto

BPE aprende tokens a partir de frecuencias del texto. Pero hay cosas que el modelo necesita saber y que no están *en* el texto: dónde termina un documento, quién habla, dónde tiene que parar.

## Conectado con

[[Vocabulario y vocab size]] · [[Token]] · [[Condición de parada]] · [[Ventana de contexto]]

---

**Leer el desarrollo:** [[1.2 — Byte Pair Encoding]] · **Índice del capítulo:** [[1.0 — Presentación del capítulo]]
