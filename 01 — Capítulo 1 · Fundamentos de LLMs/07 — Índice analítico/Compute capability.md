---
tags:
  - ficha
  - capitulo-1
seccion: "1.18"
---

# Compute capability

> **En una línea.** Es el número de versión que NVIDIA le asigna a la arquitectura de cada GPU, y determina qué operaciones soporta el hardware y si un motor de inferencia puede usarla.

> [!info] Ficha de consulta
> Esto es el índice analítico, no el libro. **El desarrollo completo está en [[1.18 — VRAM, KV cache y offload|§1.18]]**

---

## La idea, en corto

Es una versión `mayor.menor` que identifica el conjunto de capacidades de la GPU: qué tipos de datos maneja nativamente, qué instrucciones tiene, qué features de CUDA soporta.

**Tu RTX 5070 Ti está en la fila 12.0**, listada explícitamente en la documentación de Ollama.

## Conectado con

[[Ollama]] · [[VRAM]] · [[Offload a CPU]] · [[FP8]] · [[Hugging Face Hub y transformers]] · [[Modelos locales vs API]]

---

**Leer el desarrollo:** [[1.18 — VRAM, KV cache y offload]] · **Índice del capítulo:** [[1.0 — Presentación del capítulo]]
