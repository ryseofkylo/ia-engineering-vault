---
tags:
  - ficha
  - capitulo-1
seccion: "1.2"
---

# Pre-tokenización por regex

> **En una línea.** Antes de aplicar BPE, el texto se parte con una expresión regular en categorías (letras, números, puntuación, espacios) para prohibir fusiones que desperdiciarían vocabulario.

> [!info] Ficha de consulta
> Esto es el índice analítico, no el libro. **El desarrollo completo está en [[1.2 — Byte Pair Encoding|§1.2]]**

---

## La idea, en corto

Si dejaras a BPE fusionar libremente, aprendería tokens como `perro.`, `perro,`, `perro?` y `perro!` — cuatro entradas del vocabulario para la misma palabra. Un desperdicio enorme.

La solución de GPT-2 fue partir el texto primero con una regex, y correr BPE **dentro de cada pedazo, nunca a través de los bordes**. El patrón, en esencia:

## Conectado con

[[Byte Pair Encoding (BPE)]] · [[Token]] · [[Patologías de la tokenización]] · [[tiktoken y SentencePiece]]

---

**Leer el desarrollo:** [[1.2 — Byte Pair Encoding]] · **Índice del capítulo:** [[1.0 — Presentación del capítulo]]
