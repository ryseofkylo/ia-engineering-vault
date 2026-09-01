---
tags:
  - ficha
  - capitulo-1
seccion: "1.3"
---

# Patologías de la tokenización

> **En una línea.** La mayoría de los comportamientos raros de un LLM —no sabe deletrear, se equivoca en aritmética simple, se rompe con la indentación de Python— tienen una sola causa común: cómo el tokenizer partió el texto.

> [!info] Ficha de consulta
> Esto es el índice analítico, no el libro. **El desarrollo completo está en [[1.3 — Tokenizers reales y el costo de cada token|§1.3]]**
> y también se lo trata en [[1.1 — El modelo no lee texto, lee números|§1.1]].

---

## La idea, en corto

Es una lista de rarezas cuya explicación es siempre la misma.

**No sabe deletrear.** Ve `[ferro, carril]`, no letras. Contar caracteres es adivinar desde estadística, no leer.

## Conectado con

[[Token]] · [[UTF-8 y por qué el modelo no ve letras]] · [[Pre-tokenización por regex]] · [[Vocabulario y vocab size]] · [[Costo por token]]

---

**Leer el desarrollo:** [[1.3 — Tokenizers reales y el costo de cada token]] · **Índice del capítulo:** [[1.0 — Presentación del capítulo]]
