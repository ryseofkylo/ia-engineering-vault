---
tags:
  - ficha
  - capitulo-1
seccion: "1.3"
---

# Costo por token

> **En una línea.** Las APIs cobran por token de entrada y por token de salida a precios distintos, así que tu factura es una función directa de cómo el tokenizer parte tu texto — y en un modelo local el "costo" no es plata sino VRAM y latencia.

> [!info] Ficha de consulta
> Esto es el índice analítico, no el libro. **El desarrollo completo está en [[1.3 — Tokenizers reales y el costo de cada token|§1.3]]**

---

## La idea, en corto

El precio se cobra por millón de tokens, y **la salida siempre cuesta más que la entrada** (típicamente entre 3 y 5 veces más).

En un sistema RAG como `schema-rag`, la entrada domina por lejos: mandás un system prompt largo más *k* fragmentos de esquema, y recibís una query corta. La palanca de costo está casi toda del lado de la entrada.

## Conectado con

[[Token]] · [[Ventana de contexto]] · [[Vocabulario y vocab size]] · [[Patologías de la tokenización]] · [[Más contexto no es mejor]] · [[Test time compute]]

---

**Leer el desarrollo:** [[1.3 — Tokenizers reales y el costo de cada token]] · **Índice del capítulo:** [[1.0 — Presentación del capítulo]]
