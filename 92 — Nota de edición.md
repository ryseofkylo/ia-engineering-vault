---
tags:
  - indice
  - edicion
---

# Nota de edición

Cómo está construido este libro, qué se verificó y qué quedó afuera. Está acá para que dentro de seis meses puedas reconstruir el criterio, y para que si algo te chirría sepas si fue una decisión o es un error.

---

## El principio de diseño

> **El libro reemplaza a las fuentes. No las acompaña.**

La primera versión de este material era una **guía de estudio hacia las fuentes**: notas que decían "mirá el video", "leé la sección 2 del paper", "hacé las lecciones 5 y 6 del curso". Eso obligaba a saltar constantemente entre el índice y los conceptos para encontrar la sustancia, y no se parecía en nada a una lectura sostenida.

Se rehízo entero con otro criterio: **el conocimiento de cada fuente está transferido a las secciones**, desarrollado en prosa continua, con sus ejemplos, sus números y su código. [[91 — Bibliografía]] existe por trazabilidad —de dónde salió cada dato— no como lista de tareas.

Las consecuencias de ese principio, que conviene conocer:

- **Ninguna sección te manda a ningún lado.** Las referencias cruzadas ("como vimos en §1.3") son eso: referencias. Podés seguir leyendo sin ir.
- **Los enlaces a términos van al final**, en una línea aparte, para no interrumpir la lectura.
- **El índice analítico no es lectura.** Es el aparato de consulta y lo que alimenta la vista de grafo. Cada ficha dice explícitamente en qué sección se desarrolla su tema.

---

## La estructura

```
00 — Cómo leer este libro
01 — Capítulo 1 · Fundamentos de LLMs
    1.0 — Presentación del capítulo      ← índice y arco
    Parte I   · §1.1 – §1.4               ← el libro
    Parte II  · §1.5 – §1.6
    Parte III · §1.7 – §1.10
    Parte IV  · §1.11 – §1.13
    Parte V   · §1.14 – §1.19
    Cierre    · §1.20 – §1.22             ← TP, laboratorio, autoevaluación
    Índice analítico                      ← 51 fichas + la red del grafo
90 — Glosario                             ← autogenerado
91 — Bibliografía                         ← trazabilidad
92 — Nota de edición
```

**Por qué las partes son carpetas y las secciones archivos.** Las partes agrupan por tema y le dan al panel izquierdo la forma de un índice de libro. La numeración de secciones es **continua dentro del capítulo** (§1.14 es la sección 14, esté en la parte que esté), que es como numeran los manuales reales.

**Por qué cada sección tiene la misma anatomía.** Apertura que sitúa el tema, desarrollo en prosa, ejemplos y código, una sección de aplicación a `schema-rag`, errores frecuentes, resumen numerado, términos y navegación. La repetición de la estructura es deliberada: te deja saber dónde buscar sin releer.

---

## De dónde sale cada sección

| Sección | Fuente principal |
|---|---|
| §1.1 – §1.3 | Karpathy, *Let's build the GPT Tokenizer* |
| §1.4 | Karpathy + consecuencias operativas no cubiertas por él |
| §1.5 – §1.6 | Liu et al., *Lost in the Middle* |
| §1.7 – §1.10 | Chip Huyen, *Generation configurations* |
| §1.11 – §1.13 | DeepLearning.AI, *Getting Structured LLM Output* |
| §1.14 | Argumento de privacidad + consecuencia de §1.13 |
| §1.15 | Simon Frey, *What is LLM quantization?* |
| §1.16 | Hugging Face, *Quantization concepts* |
| §1.17 | Frey + Hugging Face + criterio de selección |
| §1.18 – §1.19 | Ollama, *GPU support* y FAQ |

### El orden no es el de la lista original de links

Vos numeraste las siete fuentes en el orden en que las juntaste. El libro las presenta en otro orden, siguiendo **las unidades de M1 tal como están en tu propio plan de estudios**: tokenización y ventana de contexto → degradación por posición → sampling → salida estructurada → modelos locales y cuantización.

| Orden en el libro | Fuente | En tu lista original |
|---|---|---|
| Parte I | Karpathy — tokenizer | link 1 |
| Parte II | Liu et al. — Lost in the Middle | **link 3** |
| Parte III | Chip Huyen — sampling | **link 4** |
| Parte IV | DeepLearning.AI — structured output | **link 2** |
| Parte V (primero) | Simon Frey — cuantización simple | **link 7** |
| Parte V (después) | Hugging Face — quantization concepts | link 6 |
| Parte V (último) | Ollama — GPU support | **link 5** |

Las tres razones, en una línea cada una:

- **Salida estructurada bajó al cuarto lugar** porque la técnica más fuerte (constrained decoding) funciona manipulando el vector de logits, que se explica en la parte de sampling. Antes es magia; después es obvio.
- **Lost in the Middle subió al segundo** porque corrige el error de razonamiento que induce la Parte I ("mi trabajo es hacer entrar lo máximo posible") antes de que se haga hábito.
- **La cuantización se invirtió** (7 → 6 → 5 pasó a ser Frey → HF → Ollama) porque la formalización con `scale` y `zero-point` es ruido sin la intuición previa, y la tabla de compute capability no significa nada sin saber qué es cuantizar.

**No se perdió nada:** las siete fuentes están cubiertas, y la tabla de arriba te da la traducción de un vistazo.

---

## Cobertura del plan de estudios

Las cinco unidades de M1, contra lo que hay en el libro:

| Unidad del plan | Secciones | Estado |
|---|---|---|
| Tokenización y ventana de contexto | §1.1 – §1.4 | Completo |
| Degradación por posición ("lost in the middle") | §1.5 – §1.6 | Completo |
| Sampling (temperature, top_p, `temperature=0`) | §1.7 – §1.10 | Completo |
| Salida estructurada (JSON mode, function calling, pydantic) | §1.11 – §1.13 | Completo |
| Modelos locales y open source (Ollama, HF Hub, cuantización) | §1.14 – §1.19 | Completo |

Y el enunciado del trabajo práctico:

| Del plan | Dónde |
|---|---|
| Definir el schema pydantic (sql, explicación, tablas usadas) | [[1.20 — Trabajo práctico]], paso 1 |
| Migrar el prompt actual a structured output | Paso 2 |
| Correr 20 pedidos reales y contar fallos de parseo | Paso 3 |
| Criterio: 20/20 JSON parseable, sin reintentos | [[1.22 — Autoevaluación]], sección 1 |

---

## Verificación de los datos

Todo dato numérico o textual citado salió de la fuente primaria, no de memoria:

- **Lost in the Middle** — los porcentajes (closed-book 56,1 %, oracle 88,3 %, peor caso de clave-valor 45,6 %, +1,5 % al pasar de 20 a 50 documentos), los modelos exactos (MPT-30B-Instruct, LongChat-13B-16K, GPT-3.5-Turbo 4K/16K, Claude-1.3 8K/100K) y el montaje experimental se leyeron del **PDF del paper (v3)**. Los resúmenes automáticos del abstract listaban modelos que el paper no evaluó.
- **Ollama** — la fila de compute capability 12.0 se verificó textualmente: **`RTX 5070 Ti` aparece explícitamente**, junto con RTX 5060, 5060 Ti, 5070, 5080, 5090 y las RTX PRO Blackwell. El requisito de driver (550+, y 570+ para compute 5.0–6.2) también es textual.
- **Hugging Face** — las fórmulas de `scale` y `zero-point`, el `packed_byte`, las variantes FP8 E4M3/E5M2 y el ejemplo de `BitsAndBytesConfig`.
- **Chip Huyen** — la tabla de temperature con logits `[1, 3]`, el ejemplo de top-p, el hallazgo de Cobbe et al. sobre las 400 muestras.
- **DeepLearning.AI** — las 7 lecciones con sus duraciones, los instructores y las herramientas.
- **gpt-oss:20b** — el "as little as 16GB" y el formato MXFP4 (~4,25 bits/parámetro), de la ficha oficial.

---

## Lo que quedó afuera, a propósito

Temas mencionados pero **no** desarrollados, porque pertenecen a materias posteriores:

| Tema | Materia | Por qué no acá |
|---|---|---|
| Prompt caching y versionado de prompts | M2 | Es una unidad entera de M2 |
| Compactación de historial | M2 | Ídem |
| Few-shot y chain-of-thought | M2 | Ídem |
| Cómo medir si una query es **correcta** | M3 | Este capítulo mide **parseo**, a propósito |
| Error analysis sobre traces | M3 | |
| Chunking, embeddings, reranking en profundidad | M4 | Acá se toca sólo el ángulo de posición |
| Agentes y bucles de herramientas | M5 | Function calling se explica como mecanismo, no como arquitectura |
| vLLM, throughput, concurrencia | M6 | Ollama alcanza para un usuario |
| Presupuestos de costo y latencia en producción | M7 | §1.3 da la base |

Y dos que quedaron afuera por honestidad, no por planificación:

- **Un ranking de "mejores modelos para 16 GB".** No existe fuente confiable. El único dato duro es el de `gpt-oss:20b`. Lo demás hay que medirlo con el experimento 8 del laboratorio.
- **Los números de *Lost in the Middle* aplicados a modelos actuales.** El paper es de 2023. La forma del hallazgo se sostiene; los porcentajes son de esos modelos. Está advertido dentro de §1.5.

---

## Pendientes reales

- [ ] **Las 20 preguntas del trabajo práctico.** Dependen de tu esquema; los criterios de selección están en [[1.20 — Trabajo práctico]].
- [ ] **Los resultados de los 8 experimentos.** El libro tiene los montajes; los números son tuyos.
- [ ] **Una nota por modelo local probado**, con su tabla de VRAM, tokens/s y tasa de acierto. Se arma sola con el experimento 8.

---

## Mantenimiento

**El orden del panel izquierdo** lo dan ocho archivos `sortspec.md` (raíz, capítulo, las cinco partes y el cierre), que lee el plugin **Custom File Explorer sorting**, ya habilitado y activo. No son contenido. Si algún día ves todo alfabético, el plugin está suspendido: clic en su ícono de la cinta lateral.

**El glosario se genera solo** a partir de la línea "En una línea" de cada ficha del índice analítico. Si querés cambiar una definición, cambiala en la ficha. El script está en `.obsidian/regenerar-glosario.py`.

**La verificación de coherencia** —enlaces rotos, anclas inexistentes, notas huérfanas, estructura de las fichas— se corre con `.obsidian/verificar-boveda.py`. Conviene volver a correrla al terminar cada capítulo.

---

Volver a [[00 — Cómo leer este libro]] · [[1.0 — Presentación del capítulo]]
