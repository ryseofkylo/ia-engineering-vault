---
tags:
  - ficha
  - capitulo-1
seccion: "1.16"
---

# PTQ y QAT

> **En una línea.** PTQ cuantiza el modelo **después** de entrenarlo (barato, es lo que vas a usar); QAT simula la cuantización **durante** el entrenamiento para que el modelo se adapte (mejor calidad, requiere reentrenar).

> [!info] Ficha de consulta
> Esto es el índice analítico, no el libro. **El desarrollo completo está en [[1.16 — El mecanismo de la cuantización|§1.16]]**

---

## La idea, en corto

**PTQ — Post-Training Quantization.** Agarrás un modelo ya entrenado y le bajás la precisión a los pesos. No hace falta reentrenar. Es cuestión de minutos u horas. Es lo que hace todo el ecosistema de modelos cuantizados que vas a bajar de Hugging Face o de Ollama.

Métodos de PTQ que vas a ver nombrados: **GPTQ** (cuantiza capa por capa compensando el error acumulado), **AWQ** (identifica los pesos más importantes según las activaciones y los protege), **bitsandbytes** (cuantización al vuelo al cargar), **GGUF/k-quants** (el formato de llama.cpp y Ollama).

## Conectado con

[[Cuantización]] · [[Cuantización afín]] · [[Granularidad de la cuantización]] · [[Perplexity]] · [[Hugging Face Hub y transformers]] · [[Ollama]]

---

**Leer el desarrollo:** [[1.16 — El mecanismo de la cuantización]] · **Índice del capítulo:** [[1.0 — Presentación del capítulo]]
