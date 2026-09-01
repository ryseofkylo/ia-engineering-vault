---
tags:
  - ficha
  - capitulo-1
seccion: "1.7"
---

# No determinismo del LLM

> **En una línea.** El mismo prompt puede producir respuestas distintas, porque el modelo genera una distribución de probabilidad y alguien sortea de ella — y aun eliminando el sorteo quedan otras fuentes de variación.

> [!info] Ficha de consulta
> Esto es el índice analítico, no el libro. **El desarrollo completo está en [[1.7 — Logits, softmax y azar|§1.7]]**
> y también se lo trata en [[1.8 — Temperature|§1.8]].

---

## La idea, en corto

La idea de fondo: los modelos de IA son **probabilísticos**, a diferencia de una persona a la que le preguntás dos veces lo mismo y te contesta igual. Si el modelo cree que la comida vietnamita es la mejor con un 70 % de probabilidad, la va a responder el 70 % de las veces.

1. **El sampling.** La más grande y la única que apagás del todo: poné `temperature=0`.
2. **El batching del servidor.** Tu pedido se agrupa con los de otros usuarios, y esa agrupación cambia el orden de las operaciones numéricas.
3. **La aritmética en GPU.** La suma en punto flotante no es asociativa. Con miles de operaciones en paralelo, el orden varía entre corridas y los resultados difieren en los últimos decimales. Si dos logits están casi empatados, eso alcanza para que el `argmax` elija distinto y la generación entera se bifurque.
4. **Versiones del modelo.** El mismo nombre puede apuntar a pesos actualizados sin aviso.

## Conectado con

[[Temperature]] · [[Greedy decoding y temperature 0]] · [[Alucinación]] · [[Logprobs]] · [[Test time compute]] · [[Closed-book y oracle como baselines]]

---

**Leer el desarrollo:** [[1.7 — Logits, softmax y azar]] · **Índice del capítulo:** [[1.0 — Presentación del capítulo]]
