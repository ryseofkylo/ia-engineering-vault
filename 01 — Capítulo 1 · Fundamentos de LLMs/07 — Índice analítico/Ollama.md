---
tags:
  - ficha
  - capitulo-1
seccion: "1.19"
---

# Ollama

> **En una línea.** Es la forma más simple de correr modelos abiertos en tu máquina: descarga, cuantización y servidor con API compatible con OpenAI, todo resuelto por vos.

> [!info] Ficha de consulta
> Esto es el índice analítico, no el libro. **El desarrollo completo está en [[1.19 — Ollama en la práctica|§1.19]]**
> y también se lo trata en [[1.18 — VRAM, KV cache y offload|§1.18]].

---

## La idea, en corto

1. **Un registro de modelos.** `ollama pull qwen2.5-coder:14b` y listo, ya cuantizado.
2. **Un scheduler.** Decide cuántas capas van a la GPU según la VRAM disponible, y hace [[Offload a CPU]] con el resto.
3. **Un servidor HTTP** con endpoint compatible con la API de OpenAI, así que tu código de `schema-rag` casi no cambia.

**`ollama ps` es el más importante de todos.** La columna `Processor` te dice `100% GPU`, `100% CPU`, o el reparto. Ver [[Offload a CPU]].

## Conectado con

[[Modelos locales vs API]] · [[VRAM]] · [[KV cache]] · [[Offload a CPU]] · [[Compute capability]] · [[Cuantización]] · [[Granularidad de la cuantización]] · [[Hugging Face Hub y transformers]] · [[Pesos abiertos vs open source]]

---

**Leer el desarrollo:** [[1.19 — Ollama en la práctica]] · **Índice del capítulo:** [[1.0 — Presentación del capítulo]]
