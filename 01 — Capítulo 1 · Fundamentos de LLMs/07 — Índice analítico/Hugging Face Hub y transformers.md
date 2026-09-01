---
tags:
  - ficha
  - capitulo-1
seccion: "1.17"
---

# Hugging Face Hub y transformers

> **En una línea.** El Hub es el repositorio donde vive la mayoría de los modelos abiertos, y `transformers` es la librería de Python que los carga, los cuantiza y los corre — con más control y más trabajo que Ollama.

> [!info] Ficha de consulta
> Esto es el índice analítico, no el libro. **El desarrollo completo está en [[1.17 — Elegir un modelo|§1.17]]**
> y también se lo trata en [[1.16 — El mecanismo de la cuantización|§1.16]].

---

## La idea, en corto

**El Hub** es un registro de modelos, datasets y espacios. Cada modelo tiene su ficha (*model card*) con descripción, licencia, ejemplos y —lo que más te va a servir— la lista de archivos: los pesos, la configuración y el tokenizer.

**`transformers`** es la librería que los usa. Te da control fino sobre todo: qué precisión, qué dispositivo, qué backend de cuantización, y acceso directo a los logits.

## Conectado con

[[Ollama]] · [[Cuantización]] · [[PTQ y QAT]] · [[Precisión numérica]] · [[Weight packing]] · [[Constrained decoding]] · [[tiktoken y SentencePiece]] · [[Pesos abiertos vs open source]] · [[Modelos locales vs API]]

---

**Leer el desarrollo:** [[1.17 — Elegir un modelo]] · **Índice del capítulo:** [[1.0 — Presentación del capítulo]]
