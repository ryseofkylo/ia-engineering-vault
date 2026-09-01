---
tags:
  - ficha
  - capitulo-1
seccion: "1.3"
---

# tiktoken y SentencePiece

> **En una línea.** Son las dos familias de tokenizer que vas a encontrar: `tiktoken` (OpenAI) trabaja siempre sobre bytes UTF-8, y SentencePiece (Llama y buena parte del mundo abierto) trabaja primero sobre caracteres Unicode y cae a bytes sólo para los raros.

> [!info] Ficha de consulta
> Esto es el índice analítico, no el libro. **El desarrollo completo está en [[1.3 — Tokenizers reales y el costo de cada token|§1.3]]**

---

## La idea, en corto

**tiktoken** — el enfoque de GPT. El orden es: texto → code points Unicode → **bytes UTF-8** → BPE sobre bytes. Todo carácter termina descompuesto en bytes antes de cualquier fusión. Simple, uniforme, sin casos especiales.

**SentencePiece** — el enfoque de Llama. El orden es: texto → **code points Unicode** → BPE sobre code points, con *byte fallback* para los caracteres raros. Es decir, las fusiones a nivel carácter pasan **antes** de la descomposición a bytes. Llama 2 lo configura con `character_coverage=0.99995` y `byte_fallback=true`: cubre el 99,995 % de los caracteres del corpus directamente, y el resto lo resuelve por bytes.

## Conectado con

[[Byte Pair Encoding (BPE)]] · [[UTF-8 y por qué el modelo no ve letras]] · [[Token]] · [[Vocabulario y vocab size]] · [[Hugging Face Hub y transformers]]

---

**Leer el desarrollo:** [[1.3 — Tokenizers reales y el costo de cada token]] · **Índice del capítulo:** [[1.0 — Presentación del capítulo]]
