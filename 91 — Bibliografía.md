---
tags:
  - indice
  - bibliografia
---

# Bibliografía

> [!important] Esto no es una lista de tareas
> **No hace falta que abras ninguna de estas fuentes.** Todo su contenido está desarrollado en las secciones del libro.
>
> Esta página existe por **trazabilidad**: para que sepas de dónde salió cada dato, para que puedas citar la fuente si tenés que defender una decisión, y para que sepas adónde ir el día que quieras profundizar más allá de lo que el capítulo cubre.

---

## Capítulo 1 · Fundamentos de LLMs

Siete fuentes, todas gratuitas. El plan de estudios las verificó cruzándolas contra el libro *AI Engineering* (Chip Huyen, O'Reilly), roadmap.sh y 8 avisos reales de AI Engineer remoto.

---

### 1 · Let's build the GPT Tokenizer

**Andrej Karpathy** · YouTube · ~2h13m · video con código
🔗 https://www.youtube.com/watch?v=zduSFxRajkE
📦 Código: https://github.com/karpathy/minbpe — incluye `lecture.md` (versión escrita) y `exercise.md`

**Qué aportó al libro.** Todo el material de tokenización: Unicode y UTF-8, el algoritmo BPE paso a paso, la pre-tokenización por regex de GPT-2 y GPT-4, `tiktoken`, tokens especiales, SentencePiece, y el catálogo de rarezas de los LLM que se explican por tokenización.

**Dónde está en el libro.** [[1.1 — El modelo no lee texto, lee números|§1.1]] · [[1.2 — Byte Pair Encoding|§1.2]] · [[1.3 — Tokenizers reales y el costo de cada token|§1.3]]

**Verificación.** Reseñado por Simon Willison (simonwillison.net) y discutido en Hacker News.

**Si algún día querés ir más lejos.** El ejercicio de `minbpe` te hace construir un tokenizer compatible con GPT-4 en cuatro pasos. Es la mejor forma de fijar §1.2 con las manos, si te interesa el tema más allá de lo operativo.

---

### 2 · Lost in the Middle: How Language Models Use Long Contexts

**Nelson F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, Percy Liang** (Stanford, UC Berkeley, Samaya AI) · arXiv 2307.03172, v3 de noviembre de 2023 · TACL 2024 · paper
🔗 https://arxiv.org/abs/2307.03172

**Qué aportó al libro.** El experimento completo de degradación posicional: multi-document QA sobre NaturalQuestions-Open y la tarea sintética de recuperación clave-valor. La curva en U, los baselines closed-book y oracle con sus números, la evidencia de que los modelos de contexto extendido no usan mejor su contexto, y el caso de estudio sobre cuántos documentos conviene recuperar.

**Dónde está en el libro.** [[1.5 — Lost in the Middle|§1.5]] · [[1.6 — Por qué pasa y qué hacer al respecto|§1.6]]

**Verificación.** Base citada por el reporte "Context Rot" de Chroma, que generó 260 puntos y 59 comentarios en Hacker News extendiendo el hallazgo a modelos actuales.

**Advertencia de vigencia.** Los modelos evaluados son de 2023 (GPT-3.5-Turbo, Claude-1.3, MPT-30B-Instruct, LongChat-13B). La *forma* del hallazgo se sostiene; los porcentajes no aplican a modelos de hoy. Está señalado en §1.5.

---

### 3 · Generation configurations: temperature, top-k, top-p, and test time compute

**Chip Huyen** · enero de 2024 · artículo
🔗 https://huyenchip.com/2024/01/16/sampling.html

**Qué aportó al libro.** Toda la mecánica de generación: la naturaleza probabilística del modelo, temperature con su fórmula y el ejemplo numérico de logits `[1, 3]`, top-k, top-p con el ejemplo de `sí/tal vez/no/otro`, logprobs, condiciones de parada, test time compute con el hallazgo de Cobbe et al. (2021) sobre las 400 muestras, y la introducción a constraint sampling.

**Dónde está en el libro.** [[1.7 — Logits, softmax y azar|§1.7]] · [[1.8 — Temperature|§1.8]] · [[1.9 — Top-k y top-p|§1.9]] · [[1.10 — Logprobs, parada y test time compute|§1.10]]

**Verificación.** *[inferencia]* No se encontró un hilo externo puntual sobre este post; está incluido por autoridad de la autora, no por discusión verificada. El post es un extracto del libro *AI Engineering*.

**Si algún día querés ir más lejos.** El libro completo de Chip Huyen es la referencia general del plan de estudios entero, no sólo de este capítulo.

---

### 4 · Getting Structured LLM Output

**DeepLearning.AI** con dottxt (`.txt`) · instructores **Will Kurt** (Founding Engineer) y **Cameron Pfiffer** (Developer Relations) · 1 h 21 min · 7 lecciones en video, 4 ejemplos de código y un quiz · nivel intermedio
🔗 https://www.deeplearning.ai/courses/getting-structured-llm-output/

**Qué aportó al libro.** Las cuatro estrategias de formato, JSON mode y su límite, function calling, validación con pydantic, la librería `instructor` y los reintentos, `outlines` y la generación restringida modificando logits, y las expresiones regulares como máquinas de estados finitos.

**Dónde está en el libro.** [[1.11 — Del texto libre al dato|§1.11]] · [[1.12 — Las cuatro estrategias|§1.12]] · [[1.13 — Constrained decoding|§1.13]]

**Verificación.** Anunciado por Andrew Ng en X; curso oficial de DeepLearning.AI.

**Si algún día querés ir más lejos.** Los cuatro ejemplos de código del curso son ejecutables y cubren `instructor` y `outlines` con más detalle del que el libro necesita para el trabajo práctico.

---

### 5 · What is LLM quantization? Simply explained

**Simon Frey** · publicado y actualizado en 2025 · artículo
🔗 https://simon-frey.com/blog/what-is-llm-quantization-simply-explained/

**Qué aportó al libro.** La intuición de la cuantización: la analogía del reloj, los tres pasos del proceso, la perplexity como medida del daño, y el planteo del dilema entre un modelo grande cuantizado y uno chico completo.

**Dónde está en el libro.** [[1.15 — Precisión numérica y la idea de cuantizar|§1.15]] · [[1.17 — Elegir un modelo|§1.17]]

---

### 6 · Quantization concepts

**Hugging Face** · documentación oficial de Transformers
🔗 https://huggingface.co/docs/transformers/en/quantization/concept_guide

**Qué aportó al libro.** Toda la formalización: cuantización afín simétrica y asimétrica con las fórmulas de `scale` y `zero-point`, INT4 y weight packing, FP8 (E4M3 y E5M2) y el esquema A8W8, granularidad per-tensor/per-channel/per-group, PTQ versus QAT, y el ejemplo con `BitsAndBytesConfig`.

**Dónde está en el libro.** [[1.16 — El mecanismo de la cuantización|§1.16]] · [[1.17 — Elegir un modelo|§1.17]]

**Si algún día querés ir más lejos.** La misma documentación tiene una página *Selecting a quantization method* con la comparación concreta entre backends (bitsandbytes, GPTQ, AWQ, torchao), que el libro resume pero no agota. GGUF —el formato que vas a usar con Ollama— pertenece al ecosistema de llama.cpp y no está cubierto ahí.

---

### 7 · Ollama — GPU support

**Ollama** · documentación oficial
🔗 https://docs.ollama.com/gpu
📎 https://docs.ollama.com/faq

**Qué aportó al libro.** La tabla de compute capability de NVIDIA (donde **RTX 5070 Ti** aparece explícitamente en la fila **12.0**, Blackwell), el requisito de driver 550+, las variables de entorno de selección de GPU, y —de la FAQ— `ollama ps` con su columna Processor, `num_ctx` y su default de 4096, `OLLAMA_KEEP_ALIVE` y `OLLAMA_MAX_LOADED_MODELS`.

**Dónde está en el libro.** [[1.18 — VRAM, KV cache y offload|§1.18]] · [[1.19 — Ollama en la práctica|§1.19]]

**Verificación.** Documentación oficial, verificada por consulta directa.

---

## Fuente primaria adicional

### gpt-oss (OpenAI, open-weight)

🔗 https://ollama.com/library/gpt-oss

Ficha oficial. Declara que la variante de **20B** corre en sistemas con *tan poco como 16 GB* de memoria, gracias a la cuantización **MXFP4** (~4,25 bits por parámetro sobre más del 90 % de los parámetros). Descarga: 14 GB. Ventana: 128K. La variante de 120B (65 GB) está pensada para una sola GPU de 80 GB.

**Dónde está en el libro.** [[1.15 — Precisión numérica y la idea de cuantizar|§1.15]] · [[1.17 — Elegir un modelo|§1.17]]

> [!warning] Sobre los rankings de "mejores modelos para 16 GB"
> No hay un consenso limpio y verificable. Es un espacio con mucho contenido de afiliados que se contradice entre sí. El dato de `gpt-oss:20b` es **el único de fuente primaria** que se pudo confirmar. Todo lo que vas a leer sobre modelos de 14B a 30B con offload a CPU es inferencia razonable de la comunidad, no un benchmark medido de primera mano. Probalo vos con tu hardware — para eso está el experimento 8 de [[1.21 — Laboratorio]].

---

## Referencias citadas dentro del libro

Trabajos mencionados en las secciones que no son fuentes primarias del capítulo, por si alguna vez los buscás:

- **Cobbe et al. (2021)** — el hallazgo de que muestrear hasta ~400 salidas mejora el rendimiento y más allá lo empeora. Citado en [[1.10 — Logprobs, parada y test time compute|§1.10]].
- **Contriever** (Izacard et al.) — el sistema de recuperación afinado sobre MS-MARCO que se usó para generar los distractores del experimento de *Lost in the Middle*. Citado en [[1.5 — Lost in the Middle|§1.5]].
- **NaturalQuestions-Open** (Lee et al., Kwiatkowski et al.) — el conjunto de consultas reales a Google con respuestas anotadas de Wikipedia. Citado en [[1.5 — Lost in the Middle|§1.5]].
- **Flan-T5-XXL y Flan-UL2** — los modelos encoder-decoder con los que se probó el efecto de la arquitectura. Citados en [[1.6 — Por qué pasa y qué hacer al respecto|§1.6]].
- **GPTQ, AWQ, bitsandbytes, GGUF/k-quants** — métodos y formatos de cuantización post-entrenamiento. Citados en [[1.16 — El mecanismo de la cuantización|§1.16]] y [[1.17 — Elegir un modelo|§1.17]].
- **outlines, guidance, GBNF** — herramientas de generación restringida. Citadas en [[1.13 — Constrained decoding|§1.13]].
- **instructor** — librería de reintentos con validación. Citada en [[1.12 — Las cuatro estrategias|§1.12]].
- **vLLM** — motor de inferencia orientado a concurrencia y throughput. Citado en [[1.19 — Ollama en la práctica|§1.19]] como camino posterior.

---

Volver a [[00 — Cómo leer este libro]] · [[1.0 — Presentación del capítulo]]
