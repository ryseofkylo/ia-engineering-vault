# IA Engineering — manual de estudio

Bóveda de [Obsidian](https://obsidian.md) con un manual de **AI Engineering** escrito para leerse de corrido, como un libro de facultad. Cada capítulo corresponde a una materia de un plan de estudios propio.

> **Principio de diseño:** el libro **reemplaza** a las fuentes, no las acompaña. Todo el conocimiento de la bibliografía está desarrollado adentro de las secciones. No hace falta abrir ningún enlace externo para estudiar. La bibliografía existe sólo por trazabilidad.

---

## Estado

| | |
|---|---|
| Capítulos terminados | 1 de 9 |
| Secciones de contenido | 23 |
| Fichas del índice analítico | 51 |
| Palabras | ~57.000 |
| Enlaces internos | 853 |
| Verificación | 0 enlaces rotos · 0 huérfanas · cadena de navegación completa |

### Capítulo 1 · Fundamentos de LLMs

Qué es un modelo de lenguaje visto desde afuera: qué recibe, qué hace con eso, qué devuelve y dónde corre.

| Parte | Secciones | Tema |
|---|---|---|
| I | §1.1 – §1.4 | Cómo el modelo recibe el texto — tokens, BPE, tokenizers, ventana de contexto |
| II | §1.5 – §1.6 | Qué hace con un contexto largo — degradación posicional y qué hacer al respecto |
| III | §1.7 – §1.10 | Cómo elige cada palabra — logits, temperature, top-k/top-p, logprobs |
| IV | §1.11 – §1.13 | Cómo se fuerza la forma de la salida — JSON mode, esquemas, constrained decoding |
| V | §1.14 – §1.19 | Dónde corre el modelo — local vs API, cuantización, VRAM, Ollama |
| Cierre | §1.20 – §1.22 | Trabajo práctico, laboratorio y autoevaluación |

---

## Estructura del repositorio

```
00 — Cómo leer este libro.md
01 — Capítulo 1 · Fundamentos de LLMs/
    1.0 — Presentación del capítulo.md      índice, arco del capítulo
    01 — Parte I · …/  …  05 — Parte V · …/  el libro, lectura continua
    06 — Cierre/                            TP, laboratorio, autoevaluación
    07 — Índice analítico/                  51 fichas de consulta = la red del grafo
90 — Glosario.md                            autogenerado
91 — Bibliografía.md                        trazabilidad de las fuentes
92 — Nota de edición.md                     criterio editorial y verificación
```

Cada sección de contenido tiene siempre la misma anatomía: apertura, desarrollo en prosa, ejemplos y código, bajada a un sistema real, errores frecuentes, resumen numerado, términos y pie de navegación `← Anterior / Siguiente →`.

Los `sortspec.md` no son contenido: configuran el orden del explorador de archivos.

---

## Cómo abrirlo

1. Clonar el repositorio.
2. En Obsidian: *Open folder as vault* y elegir la carpeta clonada.
3. Instalar el plugin de comunidad **Custom File Explorer sorting** (de SebastianMC). Sin él, el panel izquierdo se ordena alfabéticamente y se pierde el orden de lectura; el contenido se lee igual, y el índice completo con enlaces está en la presentación de cada capítulo.

---

## Herramientas

En `.obsidian/`, fuera de la vista de Obsidian:

| Script | Qué hace |
|---|---|
| `verificar-boveda.py` | Enlaces rotos, anclas inexistentes, notas huérfanas, cadena de navegación, estructura de secciones y fichas, consistencia de los `sortspec` |
| `regenerar-glosario.py` | Regenera `90 — Glosario.md` desde la línea "En una línea" de cada ficha |
| `PROMPT — nuevo capítulo.md` | Prompt reutilizable para agregar un capítulo siguiendo el mismo criterio |

```bash
python ".obsidian/verificar-boveda.py"
python ".obsidian/regenerar-glosario.py"
```

---

## Bibliografía del Capítulo 1

Siete fuentes, todas gratuitas. El detalle de qué aportó cada una y en qué sección está, en `91 — Bibliografía.md`.

- Andrej Karpathy — *Let's build the GPT Tokenizer*
- Liu et al. — *Lost in the Middle: How Language Models Use Long Contexts* (arXiv 2307.03172, TACL 2024)
- Chip Huyen — *Generation configurations: temperature, top-k, top-p, and test time compute*
- DeepLearning.AI con dottxt — *Getting Structured LLM Output*
- Simon Frey — *What is LLM quantization? Simply explained*
- Hugging Face — *Quantization concepts*
- Ollama — *GPU support* y FAQ
