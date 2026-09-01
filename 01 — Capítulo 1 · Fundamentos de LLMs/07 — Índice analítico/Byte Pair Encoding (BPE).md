---
tags:
  - ficha
  - capitulo-1
seccion: "1.2"
---

# Byte Pair Encoding (BPE)

> **En una línea.** BPE es el algoritmo que construye el vocabulario de un tokenizer: busca el par de símbolos consecutivos más frecuente, lo fusiona en un símbolo nuevo, y repite hasta llegar al tamaño de vocabulario deseado.

> [!info] Ficha de consulta
> Esto es el índice analítico, no el libro. **El desarrollo completo está en [[1.2 — Byte Pair Encoding|§1.2]]**

---

## La idea, en corto

1. Contar todos los pares de símbolos consecutivos que aparecen en el texto.
2. Encontrar el par **más frecuente**.
3. Crear un símbolo nuevo que represente ese par, y agregarlo al vocabulario.
4. Reemplazar todas las apariciones de ese par por el símbolo nuevo.
5. Volver al paso 1.

Cada vuelta agrega un token al vocabulario y acorta la secuencia. Si arrancás con 256 símbolos y hacés 50.000 vueltas, terminás con un vocabulario de ~50.256.

## Conectado con

[[Token]] · [[Vocabulario y vocab size]] · [[UTF-8 y por qué el modelo no ve letras]] · [[Pre-tokenización por regex]] · [[tiktoken y SentencePiece]]

---

**Leer el desarrollo:** [[1.2 — Byte Pair Encoding]] · **Índice del capítulo:** [[1.0 — Presentación del capítulo]]
